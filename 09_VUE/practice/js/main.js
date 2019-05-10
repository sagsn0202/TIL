// json-server 의 기본 접속 URI 는 아래와 같습니다. 필요에 따라 수정 가능합니다.
const HOST = "http://localhost:3000";

const app = new Vue({
  el: "#app",
  data: {
    logo: 'MO<i class="fab fa-vuejs"></i>IE',
    isMain: true,
    genres: [],
    movies: [],
    search: '',
    isDetail: false, // 현재 방식의 목록/상세 화면 전환에 사용되는 flag 입니다.
    movieDetail: {},  // 상세 화면에서 출력할 때 사용할 영화 객체입니다.
    scores: [],
    inputScore: {
      content: '',
      score: 10,
      movieId: null,
    },
  },
  methods: {
    async toggleDetail (id=null) {  // 목록 <=> 상세 화면을 전환합니다. 인자로 id 가 들어올 경우, 상세화면을 표시합니다.
      if (id) {
        // 갱신된 데이터 새로 받아서 보여주기
        // const res = await axios.get(`${HOST}/movies/${id}`);
        // this.movieDetail = res.data;

        // 그냥 아까 자료 보여주기
        this.movieDetail = this.movies.find(movie => movie.id === id);

        const res = await axios.get(`${HOST}/movies/${id}/scores`); // [ {}, {}, {} ]
        this.scores = res.data;
      }
      this.isDetail = !this.isDetail
    },

    async getMovies (genreId=null, options=null) {
      let URL = `${HOST}/movies`;
      if (options) {
        URL = `${HOST}/movies?_sort=${options.sort}&_order=${options.order}`
      } else if (genreId) {
        URL = `${HOST}/genres/${genreId}/movies`
      }
      const res = await axios.get(URL);
      this.movies = res.data;
    },

    async postScore(movieId) {
      function getAverageScore(scores=[]) {
        const result = scores.reduce((acc, score) => {
          acc.total += score.score;
          acc.count++;
          return acc
        }, {total: 0, count: 0});
        return (result.total / result.count).toFixed(1)
      }

      if (this.inputScore.content && this.inputScore.score) {
        this.inputScore.movieId = movieId;
        let res = await axios.post(`${HOST}/scores`, this.inputScore);
        const newScore = res.data;  // { id: N, score: N, content: String, movieId: N }
        this.inputScore = { content: '', score: 10 };
        this.scores.push(newScore);

        res = await axios.patch(`${HOST}/movies/${movieId}`, {
          averageScore: getAverageScore(this.scores)
        });
        this.movieDetail = res.data;
      } else {
        alert('점수와 리뷰를 입력하세요.');
      }
    },
  },
  computed: {},

  watch: {
    async search (keyword) {
      if (keyword) {
        const URL = `${HOST}/movies?q=${keyword}`;
        const res = await axios.get(URL);
        this.movies = res.data;
      } else {
        this.movies = [];
      }
    },
    movies () {
      this.isDetail = false;
    }
  },

  /* Vue Instance LIFE CYCLE */

  async created () {  // Vue 인스턴스가 생성되는 시점에 실행되는 함수입니다. 현재는 Vue 인스턴스가 생성되면, json-server 에서 장르목록만 받아옵니다.
    const res = await axios.get(`${HOST}/genres`);
    this.genres = res.data;
  }
});

document.addEventListener('keyup', e => {
  if (e.key === 'Escape') app.$data.isDetail = false;
});
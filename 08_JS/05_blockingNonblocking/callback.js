// const listUsers = () => {
//     setTimeout(() => {
//         const users = [
//             { id: 1, githubID: 'eduyu' },
//             { id: 2, githubID: 'edujohn' },
//         ];
//         return users;
//     }, 2000)
// };

function getUser (id, callback) {
    setTimeout(() => {
        const users = [
            { id: 1, githubID: 'eduyu' },
            { id: 2, githubID: 'edujohn' },
        ];
        const user = users.find(user => user.id === id);
        console.log('Data Loaded!');
        console.log(user);
        callback(user);
    }, 2000)
}

function getRepos (user, callback) {
    setTimeout(() => {
        const repos = [
            'TIL',
            'Workshop_HW',
            'Python',
            'JS',
        ];
        console.log('Data Loaded!');
        console.log(repos);
        callback(repos)
    }, 2000)
}

function getCommits (repo, callback) {
    setTimeout(() => {
        const commits = [
            'init repo',
            'Make index.html',
        ];
        console.log('Data Loaded!');
        console.log(commits);
        callback(commits);
    }, 2000)
}

getUser(1, user => {
    getRepos(user, repos => {
        getCommits(repos[0], commits => {
            console.log(commits.length)
        });
    });
});

// const user = { id: 1, githubID: 'eduyu'};
// getRepos(user, (repos) => {
//    console.log(repos);
// });

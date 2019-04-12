## 복습

### 정보이론 기초

#### 개요

정보이론은 시그널에 존재하는 정보의 양을 측정하는 응용수학의 한 갈래입니다. 정보이론은 무선전송을 통해 알파벳으로 된 메시지를 보내려는 연구에서 시작되었습니다. 이 때 정보이론은 최적의 코드를 디자인하고, 메시지의 기대 길이(expected length)를 계산하는 데 도움이 됩니다. 머신러닝에서는 해당 확률분포의 특성을 알아내거나 확률분포 간 유사성을 정량화하는 데 쓰입니다.

정보이론의 핵심 아이디어는 잘 일어나지 않는 사건(unlikely event)은 자주 발생하는 사건보다 정보량이 많다(informative)는 것입니다. 예컨대 ‘아침에 해가 뜬다’는 메세지로 보낼 필요가 없을 정도로 정보 가치가 없습니다. 그러나 ‘오늘 아침에 일식이 있었다’는 메세지는 정보량 측면에서 매우 중요한 사건입니다. 이 아이디어를 공식화해서 표현하면 다음과 같습니다.

- 자주 발생하는 사건은 낮은 정보량을 가진다. 발생이 보장된 사건은 그 내용에 상관없이 전혀 정보가 없다는 걸 뜻한다.
- 덜 자주 발생하는 사건은 더 높은 정보량을 가진다.
- 독립사건(independent event)은 추가적인 정보량(additive information)을 가진다. 예컨대 동전을 던져 앞면이 두번 나오는 사건에 대한 정보량은 동전을 던져 앞면이 한번 나오는 정보량의 두 배이다.

#### Shannon entropy

위 세 가지 조건을 만족하는 함수는 발생 가능한 사건이나 메세지의 확률분포에 음의 로그를 취한 수식입니다. 확률변수 X의 값이 x인 사건의 정보량은 아래와 같습니다.

$I(x)=−logP(x)$

**섀넌 엔트로피(Shannon entropy)**는 모든 사건 정보량의 기대값을 뜻합니다. 전체 사건의 확률분포의 불확실성의 양을 나타낼 때 씁니다. 어떤 확률분포 P에 대한 섀넌 엔트로피 H(P)는 다음과 같습니다.

$H(P)=H(x)=E_{X∼P}[I(x)]=−E_{X∼P}[logP(x)]​$

#### KL Divergence

$D_{KL}(P||Q)=E_{X∼P}[log\frac{P(x)}{Q(x)}]=E_{X∼P}[logP(x)−logQ(x)]$

P와 Q가 동일한 확률분포일 경우 KLD는 정의에 따라 그 값이 0이 됩니다. 하지만 KLD는 비대칭(not symmetric)으로 P와 Q 위치가 뒤바뀌면 KLD 값도 달라집니다. 따라서 KLD는 거리함수로는 사용할 수 없습니다.

#### 크로스 엔트로피

KLD는 딥러닝 모델의 손실함수(loss function)로 자주 쓰이는 크로스 엔트로피(cross entropy)와 깊은 관련을 맺고 있습니다. P와 Q에 대한 크로스 엔트로피 H(P, Q)와 KLD와의 관계식은 다음과 같습니다.

$H(P,Q)=H(P)+DKL(P||Q)$

딥러닝 모델을 학습할 때 크로스 엔트로피를 최소화하는 방향으로 파라메터(가중치)들을 업데이트 합니다. 그런데 Q에 대해 크로스 엔트로피를 최소화한다는 것은 KLD를 최소화하는 것과 그 의미가 완전히 같습니다(equivalent). 왜냐하면 P는 실제 데이터의 분포를 가리키는데, P가 학습 과정에서 바뀌는 것이 아니기 때문입니다.

어쨌든 크로스 엔트로피 최소화는 KLD 최소화와 같은 의미이며 실제 데이터의 분포 P(x)와 모델이 추정한 데이터의 분포 Q(x)Q(x) 간에 차이를 최소화한다는 정도로 이해하면 좋을 것 같습니다. 딥러닝 모델의 입력값으로 쓰이는 관측치는 이산변수(discrete variable)에 해당하므로 크로스 엔트로피 H(P,Q)의 식을 다시 쓰면 다음과 같습니다.

$H(P,Q)=−E_{X∼P}[logQ(x)]=−∑xP(x)logQ(x)$

보시다시피 H(P,Q)는 P의 엔트로피인 H(P)와 유사한 꼴이나 로그 바깥에 곱해지는 확률이 P(x)이고, 로그 안에 들어가는 것이 Q(x)인 것을 확인할 수 있습니다. 두 확률분포가 교차로 곱해진다는 의미로 크로스(cross) 엔트로피라는 이름이 붙었습니다.



## 공부

CLASS*[`torch.nn.Sequential`(**args*)](https://pytorch.org/docs/stable/_modules/torch/nn/modules/container.html#Sequential)

A sequential container. Modules will be added to it in the order they are passed in the constructor. Alternatively, an ordered dict of modules can also be passed in.

To make it easier to understand, here is a small example:

```
# Example of using Sequential
model = nn.Sequential(
          nn.Conv2d(1,20,5),
          nn.ReLU(),
          nn.Conv2d(20,64,5),
          nn.ReLU()
        )

# Example of using Sequential with OrderedDict
model = nn.Sequential(OrderedDict([
          ('conv1', nn.Conv2d(1,20,5)),
          ('relu1', nn.ReLU()),
          ('conv2', nn.Conv2d(20,64,5)),
          ('relu2', nn.ReLU())
        ]))
```

## [`OrderedDict`](https://docs.python.org/3.7/library/collections.html#collections.OrderedDict)

Ordered dictionaries are just like regular dictionaries but have some extra capabilities relating to ordering operations. They have become less important now that the built-in [`dict`](https://docs.python.org/3.7/library/stdtypes.html#dict) class gained the ability to remember insertion order (this new behavior became guaranteed in Python 3.7).

Some differences from [`dict`](https://docs.python.org/3.7/library/stdtypes.html#dict) still remain:

- The regular [`dict`](https://docs.python.org/3.7/library/stdtypes.html#dict) was designed to be very good at mapping operations. Tracking insertion order was secondary.
- The [`OrderedDict`](https://docs.python.org/3.7/library/collections.html#collections.OrderedDict) was designed to be good at reordering operations. Space efficiency, iteration speed, and the performance of update operations were secondary.
- The equality operation for [`OrderedDict`](https://docs.python.org/3.7/library/collections.html#collections.OrderedDict) checks for matching order.
- The `popitem()` method of [`OrderedDict`](https://docs.python.org/3.7/library/collections.html#collections.OrderedDict) has a different signature. It accepts an optional argument to specify which item is popped.
- [`OrderedDict`](https://docs.python.org/3.7/library/collections.html#collections.OrderedDict) has a `move_to_end()` method to efficiently reposition an element to an endpoint.
- Until Python 3.8, [`dict`](https://docs.python.org/3.7/library/stdtypes.html#dict) lacked a [`__reversed__()`](https://docs.python.org/3.7/reference/datamodel.html#object.__reversed__) method.



*CLASS*[`torch.nn.LogSoftmax`(*dim=None*)](https://pytorch.org/docs/stable/_modules/torch/nn/modules/activation.html#LogSoftmax)

Applies the $\log(\text{Softmax}(x))$ function to an n-dimensional input Tensor. The LogSoftmax formulation can be simplified as:

$\text{LogSoftmax}(x_{i}) = \log\left(\frac{\exp(x_i) }{ \sum_j \exp(x_j)} \right)$

- Shape:

  Input: any shape

  Output: same as input

| Argument    | Description                                                  |
| ----------- | ------------------------------------------------------------ |
| Parameters: | **dim** ([*int*](https://docs.python.org/3/library/functions.html#int)) – A dimension along which Softmax will be computed (so every slice along dim will sum to 1). |
| Returns:    | a Tensor of the same dimension and shape as the input with values in the range [-inf, 0) |



**Maximum likelihood estimation**

최대우도추정(maximum likelihood estimation)이란 모수(parameter)가 미지의 θ인 확률분포에서 뽑은 표본(관측치) x들을 바탕으로 θ를 추정하는 기법입니다. 여기에서 우도(likelihood)란 이미 주어진 표본 x들에 비추어 봤을 때 모집단의 모수 θ에 대한 추정이 그럴듯한 정도를 가리킵니다. 우도 L(θ|x)는 θ가 전제되었을 때 표본 x가 등장할 확률인 p(x|θ)에 비례합니다.

이항분포의 확률함수는 다음과 같습니다.

$p(x)=\binom{n}{x}p^x(1−p)^{n−x}$

우선 이 동전이 공정하다(θ=0.5)고 가정하고 앞면이 56번 나왔을 때(x=56) 우도를 계산해보겠습니다.

$p(X=56|θ=0.5)=\binom{100}{56}0.5^{56}0.5^{44}≈0.0389​$

그래프를 그려보면 다음과 같습니다.

![max_likeli_image]https://i.imgur.com/qa6ikOG.png

**vs KL-Divergence**

학습데이터의 분포를 $P_{data}​$, 모델이 예측한 결과의 분포를 $P_{model}​$, 모델의 모수(파라메터)를 θ라고 두면 최대우도추정은 다음과 같이 쓸 수 있습니다. 

$θ_{ML}=argmax_{θ}P_{model}(X|θ)​$

확률은 1보다 작기 때문에 계속 곱하면 그 값이 지나치게 작아져 언더플로우(underflow) 문제가 발생하므로 로그를 취합니다. 로그우도의 기대값은 로그우도의 합에 데이터 개수(m)로 나누어 구합니다. 그런데 전체 값에 로그를 취하거나 스케일을 하여도 대소관계는 변하지는 않으므로 

$θ_{ML}=argmax_θ{E_{X∼\hat{P} data}[logP_{model}(x|θ)]}$

쿨백-라이블러 발산(Kullback-Leibler divergence, KLD)은 두 확률분포의 차이를 계산하는 데 사용하는 함수입니다. 딥러닝 모델을 만들 때 예로 들면 우리가 가지고 있는 데이터의 분포 $P_{data}$와 모델이 추정한 데이터의 분포 $P_{model}$ 간에 차이를 KLD를 활용해 구할 수 있고, KLD를 최소화하는 것이 모델의 학습 과정이 되겠습니다. KLD의 식은 다음과 같이 정의됩니다.

$D_{KL}(P||Q)=E_{X∼\hat{P}_{data}}[log⁡\hat{P}_{data}(x)−log⁡P_{model}(x)]$

​		$=−E_{X∼\hat{P}_{data}}[logP_{model}(x)]$

식을 비교해서 보면 **크로스 엔트로피(혹은 KLD) 최소화**가 **우도의 최대화**와 본질적으로 같습니다. 이 때문에 최대우도추정은 실제 데이터의 분포와 모델이 추정한 데이터의 분포를 가장 유사하게 만들어주는 모수(파라메터)를 찾아내는 방법이라고 봐도 됩니다.

**vs Mean Squared Error**

머신러닝에서는 주로 조건부 우도를 최대화하는 방식으로 학습을 합니다. 입력값 X와 모델의 파라메터 θ가 주어졌을 때 정답 Y가 나타날 확률을 최대화하는 θ를 찾는 것입니다. 실제 데이터가 학습 과정에서 바뀌는 것은 아니므로 X와 Y는 고정된 상태입니다. 모델에 X를 넣었을 때 실제 Y에 가장 가깝게 반환하는 θ를 찾아내는 것이 관건이라고 볼 수 있겠습니다. m개의 모든 관측치가 i.i.d(independent and identically distributed)라고 가정하고, 언더플로우(underflow) 방지를 위해 우도에 로그를 취한다면 최대우도추정 식은 다음과 정리할 수 있습니다.

$θ_{ML}=argmax_{θ}P_{model}(Y|X;θ)=argmax_θ∑_{i=1}mlogP_{model}(yi|xi;θ)$

여기에서 P_{model}이 가우시안 확률함수라고 가정을 해봅시다. 다시 말해 X와 Y가 정규분포를 따를 것이라고 가정해 보는 것입니다. 그러면 정규분포 확률함수로부터 이 모델의 로그우도 합은 다음과 같이 쓸 수 있습니다. (분산 σ2도 고정돼 있다고 가정, 사용자가 특정 상수값으로 지정)

$∑_{i=1}^mlogP_{model}(yi|xi;θ)=−mlogσ−\frac{m}{2}log2π−∑_{i=1}^m\frac{‖\hat{y}_i−y_i‖}{2σ^2}$

선형회귀(liner regression)의 목적식은 평균제곱오차(Mean Squared Error)입니다. MSE의 식은 다음과 같이 정의됩니다.

$MSE=\frac{1}{m}∑_{i=1}^m‖ŷ i−yi‖^2$

로그우도 합의 수식에서 세 개의 term 가운데 앞의 두 개의 term은 모두 상수값으로 학습과정에서 변하는 값이 아니며 로그우도의 합을 최대화하는 데 영향을 끼치는 term이 아닙니다. 사용자가 지정한 σ, 데이터 개수 m은 모두 상수값이므로, 우도를 최대화하는 모수(파라메터)와 평균제곱오차를 최소화하는 모수가 본질적으로 동일하다는 이야기가 됩니다.

**최대우도추정**

최대우도추정 기법으로 추정한 모수는 **일치성(consistency)**과 **효율성(efficiency)**이라는 좋은 특성을 가지고 있다고 합니다. 일치성이란 추정에 사용하는 표본의 크기가 커질 수록 진짜 모수값에 수렴하는 특성을 가리킵니다. 효율성이란 일치성 등에서 같은 추정량 가운데서도 분산이 작은 특성을 나타냅니다. 추정량의 효율성을 따질 때는 보통 평균제곱오차(MSE)를 기준으로 하는데, 크래머-라오 하한 정리에 의하면 *일치성을 가진 추정량 가운데 최대우도추정량보다 낮은 MSE를 지닌 추정량이 존재하지 않는다*고 합니다.

이러한 이유로 머신러닝에서는 모수를 추정할 때 최대우도추정 기법을 자주 쓴다고 합니다. 하지만 최대우도추정은 관측치(표본)에 큰 영향을 받기 때문에 이를 보완하는 다양한 기법이 제안되었습니다.



**음의 로그우도(negative log-likelihood)**

* 확률론적 접근

딥러닝 모델을 학습시키기 위해 최대우도추정(Maximum Likelihood Estimation) 기법을 씁니다. 입력값 X와 파라메터 θ가 주어졌을 때 정답 Y가 나타날 확률, 즉 우도 P(Y|X;θ)를 최대화하는 θ가 바로 우리가 찾고 싶은 결과입니다.

학습데이터 각각의 우도를 스케일해도 전체 *argmax*의 결과는 바뀌지 않으므로,

‘우도의 곱을 최대’로 만드는 θ == ‘로그우도의 기대값, 즉 $Σ_xP(y|x)log⁡P(y|x;θ)$를 최대’로 하는 θ

입니다.

Deep Learning Book 128페이지

> The argmax does not change when we rescale the cost function, we can divide by the total number of data to obtain a version of the criterion that is expressed as an expectation with respect to the empirical distribution $P_{data}$ defined by the training data.

다범주 분류를 학습하는 딥러닝 모델은 소프트맥스 함수를 적용합니다.

$P(y_i|x_i;θ)=\frac{f(x_i)}{∑_jexp{f(x_j)}}$ 위 식에서 f는 범주 수만큼의 차원을 갖는 벡터로써 unnormalized log probabilities에 해당합니다. 소프트맥스 함수가 취해짐으로써 그 요소의 합이 1이 됩니다. 정답 인덱스에 해당하는 f의 요소값을 높인다는 말은 최대우도추정을 수행한다는 의미로 해석할 수 있습니다.

* 정보이론의 접근

두 확률분포 p와 q 사이의 차이를 계산하는 데에는 크로스 엔트로피(cross entropy)라는 함수가 사용됩니다. 식은 −Σp(x)logq(x)입니다. 여기에서 p를 우리가 가진 데이터의 분포 P(Y|X), q를 모델이 예측한 결과의 분포 P(Y|X;θ)로 두겠습니다. 이렇게 되면 크로스 엔트로피는 파라메터 θ 하에서의 음의 로그우도의 기대값이라고 해석할 수 있습니다. 따라서 −ΣxP(y|x)log⁡P(y|x;θ)를 최소화하는 θ가 바로 우리가 찾고 싶은 모델이 됩니다.

우도의 곱이 최대인 모델을 찾는 것 == 로그우도의 기대값이 최대인 모델을 찾는 것 == 크로스 엔트로피를 최소화하는 것 그러므로 **음의 로그우도가 딥러닝 모델의 손실함수가 되는 것**입니다.



https://ratsgo.github.io/deep%20learning/2017/09/24/loss/

http://jaejunyoo.blogspot.com/2018/02/minimizing-negative-log-likelihood-in-kor-3.html



CLASS*`torch.nn.CrossEntropyLoss`(*weight=None*, *size_average=None*, *ignore_index=-100*, *reduce=None*, *reduction='mean'*)[[SOURCE\]](https://pytorch.org/docs/stable/_modules/torch/nn/modules/loss.html#CrossEntropyLoss)

This criterion combines `nn.LogSoftmax()` and `nn.NLLLoss()` in one single class.

It is useful when training a classification problem with C classes. If provided, the optional argument `weight` should be a 1D Tensor assigning weight to each of the classes. This is particularly useful when you have an unbalanced training set.

The input is expected to contain scores for each class.

input has to be a Tensor of size either (minibatch, C)(*m**i**n**i**b**a**t**c**h*,*C*) or (minibatch, C, d_1, d_2, ..., d_K)(*m**i**n**i**b**a**t**c**h*,*C*,*d*1,*d*2,...,*d**K*) with K \geq 2*K*≥2 for the K-dimensional case (described later).

This criterion expects a class index (0 to C-1) as the target for each value of a 1D tensor of size minibatch

The loss can be described as:

\text{loss}(x, class) = -\log\left(\frac{\exp(x[class])}{\sum_j \exp(x[j])}\right) = -x[class] + \log\left(\sum_j \exp(x[j])\right)loss(*x*,*c**l**a**s**s*)=−log(∑*j*exp(*x*[*j*])exp(*x*[*c**l**a**s**s*]))=−*x*[*c**l**a**s**s*]+log(*j*∑exp(*x*[*j*]))

or in the case of the weight argument being specified:

\text{loss}(x, class) = weight[class] \left(-x[class] + \log\left(\sum_j \exp(x[j])\right)\right)loss(*x*,*c**l**a**s**s*)=*w**e**i**g**h**t*[*c**l**a**s**s*](−*x*[*c**l**a**s**s*]+log(*j*∑exp(*x*[*j*])))

The losses are averaged across observations for each minibatch.

Can also be used for higher dimension inputs, such as 2D images, by providing an input of size (minibatch, C, d_1, d_2, ..., d_K)(*m**i**n**i**b**a**t**c**h*,*C*,*d*1,*d*2,...,*d**K*) with K \geq 2*K*≥2, where K*K* is the number of dimensions, and a target of appropriate shape (see below).

| Parameters: | **weight** ([*Tensor*](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)*,* *optional*) – a manual rescaling weight given to each class. If given, has to be a Tensor of size C**size_average** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,* *optional*) – Deprecated (see `reduction`). By default, the losses are averaged over each loss element in the batch. Note that for some losses, there multiple elements per sample. If the field `size_average` is set to `False`, the losses are instead summed for each minibatch. Ignored when reduce is `False`. Default: `True`**ignore_index** ([*int*](https://docs.python.org/3/library/functions.html#int)*,* *optional*) – Specifies a target value that is ignored and does not contribute to the input gradient. When size_average is `True`, the loss is averaged over non-ignored targets.**reduce** ([*bool*](https://docs.python.org/3/library/functions.html#bool)*,* *optional*) – Deprecated (see `reduction`). By default, the losses are averaged or summed over observations for each minibatch depending on `size_average`. When `reduce` is `False`, returns a loss per batch element instead and ignores `size_average`. Default: `True`**reduction** (*string**,* *optional*) – Specifies the reduction to apply to the output: ‘none’ | ‘mean’ | ‘sum’. ‘none’: no reduction will be applied, ‘mean’: the sum of the output will be divided by the number of elements in the output, ‘sum’: the output will be summed. Note: `size_average` and `reduce` are in the process of being deprecated, and in the meantime, specifying either of those two args will override `reduction`. Default: ‘mean’ |
| ----------- | ------------------------------------------------------------ |
|             |                                                              |

- Shape:

  Input: (N, C)(*N*,*C*) where C = number of classes, or(N, C, d_1, d_2, ..., d_K)(*N*,*C*,*d*1,*d*2,...,*d**K*) with K \geq 2*K*≥2 in the case of K-dimensional loss.Target: (N)(*N*) where each value is 0 \leq \text{targets}[i] \leq C-10≤targets[*i*]≤*C*−1, or(N, d_1, d_2, ..., d_K)(*N*,*d*1,*d*2,...,*d**K*) with K \geq 2*K*≥2 in the case of K-dimensional loss.Output: scalar. If reduce is `False`, then the same sizeas the target: (N)(*N*), or (N, d_1, d_2, ..., d_K)(*N*,*d*1,*d*2,...,*d**K*) with K \geq 2*K*≥2 in the case of K-dimensional loss.

Examples:

```
>>> loss = nn.CrossEntropyLoss()
>>> input = torch.randn(3, 5, requires_grad=True)
>>> target = torch.empty(3, dtype=torch.long).random_(5)
>>> output = loss(input, target)
>>> output.backward()
```
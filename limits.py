# -*- coding: utf-8 -*-
"""limits.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mablR6TLzcZiLewcWnHSh8knStQZOkMU
"""

#importando as bibliotecas
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
print("feito")

"""#Demonstração do Conceito de Limite"""

# criando um símbolo algébrico para cálculo simbólico
x=sp.Symbol('x')
#definir uma função para escrever menos
def funcao(x):
    return (x + 2) / (x + 3)

print("feito")

conjx = np.linspace(-2, -3, 100, False)
conjx2 = np.linspace(-2.5, -3, 3000, False)
print(conjx)

plt.figure(1, figsize=(14,3))
plt.plot(conjx, funcao(conjx))
plt.show()

plt.figure(1, figsize=(14,3))
plt.plot(conjx2, funcao(conjx2))
#ajustando os limites do gráfico no eixo x
plt.xlim((-3.005, -2.99))
plt.show()

sp.limit(funcao(x),x,-3)

"""Calculando: $$\lim_{x \to 0} \frac{sin(x)}{x}$$"""

funcao=sp.sin(x)/x
L=sp.limit(funcao,x,0)
print("O limite é:",L)

"""Calcule o limit de: $$\lim_{y \to 0} \frac{sin(2y)}{y}$$"""

y = sp.Symbol('y')
funcao=sp.sin(2*y)/y
L=sp.limit(funcao,y,0)
print("O limite é:",L)

"""Calcule:$$\lim_{x \to 0}1/x$$ e $$\lim_{x \to 0} \sqrt{x}$$ e $$\lim_{x \to 0} e^x$$

"""







"""O sympy tem a sua própria função de plotagem. Não é tão flexivel quanto o matplotlib."""

sp.plot(x**2, line_color='red')

sp.plot(sp.sqrt(x), line_color='red')

"""Também podemos calcular o limite nos aproximando pela esqueda, ou pela direita. Por exemplo, vamos ver $$\lim_{x \to 0} \frac{1}{x}$$"""

sp.limit(1/x, x, 0)

sp.limit(1/x, x, 0, '-')

sp.limit(1/x, x, 0, '+')

print(sp.limit(3*x-8, x, 3))

"""# Representação Formal
Considere $f_{(x)}$ uma função definida em um intervalo aberto que contém $x=a$ exceto, talvez, no ponto $x=a$, sendo assim, podemos dizer que:  

$$L=\lim_{x \to a} f_{(x)}$$

Se, neste domínio, para todo número $\varepsilon > 0$ existe um número $\delta > 0$ de tal forma que: 
se $0<|x-a|<\delta$ então $|f_{(x)} - L| < \varepsilon$. Ou, em boa matemática:

$$\forall \space \varepsilon > 0 \space\space \exists\space \delta > 0 | $$

Se $0<|x-a|<\delta$ então $|f_{(x)} - L| < \varepsilon$

Obseve que vamos igorar o ponto $x=a$ por que o cálculo do limite não se interessa pelo ponto em si. O limite se interessa apenas por aquilo que está acontecendo em torno do ponto. Ainda assim, a definição parece um tanto complexa. Ela envolve um quantificador universal $(\forall )$: para todo número $\varepsilon > 0$; um quantificador existencial $(\exists )$: existe um número $\delta > 0$; e uma condicional: se $0<|x-a|<\delta$ então $|f_{(x)} - L| < \varepsilon $. Felizmente, podemos tentar ler esta definição em bom português. 

Para cada distância positiva $\varepsilon$ de $L$ (para todo número $\varepsilon > 0$);
Existe uma distância positiva $\delta$ de $a$ (existe um número $\delta > 0$)
De tal forma que:  se $x$ está mais próximo de $a$ que a distância $\delta$ e $x \neq a$ então $f_{(x)}$ está mais próximo de $L$ que $\varepsilon$.

Considere a figura a seguir: 



---


![limites2.png](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAbgAAAEcCAYAAAC1R6FLAAABhWlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw0AcxV/TakUqDmYQUchQnayIijhKFYtgobQVWnUwufRDaNKQpLg4Cq4FBz8Wqw4uzro6uAqC4AeIm5uToouU+L+00CLGg+N+vLv3uHsHCLUS06zAOKDptpmMRaVMdkUKviKATogYwpjMLCOeWkjDc3zdw8fXuwjP8j735+hRcxYDfBLxLDNMm3ideHrTNjjvE4usKKvE58SjJl2Q+JHrSoPfOBdcFnimaKaTc8QisVRoY6WNWdHUiKeIw6qmU76QabDKeYuzVqqw5j35C0M5fTnFdZqDiGERcSQgQUEFGyjBRoRWnRQLSdqPevgHXH+CXAq5NsDIMY8yNMiuH/wPfndr5ScnGkmhKNDx4jgfw0BwF6hXHef72HHqJ4D/GbjSW/5yDZj5JL3a0sJHQO82cHHd0pQ94HIH6H8yZFN2JT9NIZ8H3s/om7JA3y3QvdrorbmP0wcgTV0t3QAHh8BIgbLXPN7d1d7bv2ea/f0AkspytBbps5cAAAAGYktHRAD/AP8A/6C9p5MAAAAJcEhZcwAAPYQAAD2EAdWsr3QAACAASURBVHja7d15fFTV/f/x10wmyWTf90AICYFACEFWERFxK7X9FgF3q7Vu/Kpfv7XV2tbWqlVbq7Vqi7Vqa1VUVLSurQouIGBBFtmXBAIBEhKSTEK22e/vjyvRMEMAIZDl/Xw88hAnyZ3MZ+7c9z3nnnOuhW+uIDo6en1xcXEoIiIi3YRhGKxcuRLbsWzk3HPP5cUXX8RqtaqiIiLSLXg8Hs4+++xjCzir1YrNZiMkJEQVFRGRbsNisaCml4iI9EoKOBERUcCJiIgo4ERERBRwx4/f78ftduP3+zs87vP5juj3DcMI+F0REVHAnVQul4t33nmHv/3tb7z66qvtQdXY2Mjs2bPZt2/fYbfR0NDAu+++qz1DREQB1z0YhsGHH35IXl4eI0eO5J133sHj8QCwefNmPvnkE8LCwg67nYULFzJ79mz27t2rvUNERAF38nm9XlJTU8nLy2PJkiWUlJQQFhaGz+fj888/p6CggNjY2E63UV9fz9NPP83777/PggULtHeIiCjgTr7Q0FBGjx5NY2Mjr7zyCueeey4Wi4W2tjYWLFjApEmTsFgsnbYAFy5c2N49OWfOHLXiREQUcN1HeXk5OTk55OTkALBnzx62bdvG4MGDO/09h8PBM8880/7/asWJiCjguhW3201ERAShoaHtrbfRo0eTlZXVaevt008/5e233+7wuFpxIiIKuG6jpKSE0047jeeee45//OMfvPDCC5x66qnY7fZD/k5DQwNPP/10wOPvv/8+H330kfYSEREF3Mm1f/9+Fi9ezMUXX8w111zD1KlTCQsLY9KkSZ3+3qJFi3jnnXeCfu/555+nurpae4qISA9j600vZvny5dx77708//zzWK1Wnn32WX7yk590ev2tqamJt956iylTpgBmF+fWrVspKioCwOl0smTJEqZPn669RUREAXdyFBcXc9lllzF//nzCw8O55JJLGDx4cKejJ8PDw/njH//Y/v91dXU88MADPPjggxiGYTZzrVYMw+h0OyIiooDrMqmpqdx4443tYXQkgRQWFtZhArjH4yE8PJy4uDjtHSIiCrju40iDTUREejfdTUBERBRwIiIiCjgREREFnIiIiAJOREREASciIgo4ERERBZyIiIgCTkRERAEnIiKigBMREVHAiYiIAk5EREQBJyIiooATERFRwImIiCjgREREFHAiIqKAExERUcCJiIgo4ERE5KQyDNi2DbxeBZyIiPQibjfceSe0tirgRESklwWcy9U7X5sCTkSkD/N4zC8FnIiI9CoHrr1ZLAo4ERHpZQFn7aVJoIATEenDfD4IDVULTkREemHA2e0KOBER6WX8foiKUsCJiEgv4/VCRgbYbAo4ERHpRdxuM9zUghMRkS5uUXkpLS1l+fLlOJ3OLn8+j8e8BtcbR1Iq4EREupFVq1Yxe/Zs7rvvPlasWNHlz+fzQVxc7ww4m3YnEZHu03p76aWXmDhxIvn5+eTk5HT5c1ZVQURE7+yiVMCJiHQTDoeD0tJSbr/9dtLT00/Ic+7YAf379856qotSROQk8/v9VFZWsnHjRqqqqqipqaGmpuaEPHddHaSkKOBERKQLGIZBdXU1y5YtY9SoUTQ2NuJwODAMAwCPx4PP5zvk77tcrvafPbrnhf37FXAiItJFQkJCGDlyJImJiZx66qmcfvrpDB48GIvFgsvlYtGiRXg6WfJ/+/btlJWVHfXz+nzQ0GBO9FbAiYhIl/D5fKxfv54BAwZ0eHzp0qUMGDAAu91+yN8d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)


---

O que a definição nos diz é que podemos pegar qualquer número $\varepsilon >0$ nós podemos ir ao gráfico da função e marcar duas linhas horizontais, $L-\varepsilon$ e $L+\varepsilon$ e, da mesma forma, exite un número $\delta >0$ que podemos escolher e traçar duas linhas verticais $a-\delta$ e $a+\delta$. 

Se escolhermos qualquer $x$ entre $a-\delta$ e $a+\delta$ então, este $x$ escolhido estará mais próximo de $a$ que $a-\delta$ e $a+\delta$. O que pode ser escrito como: $$|x-a| <\delta$$. 

Uma vez que este $x$ tenha sido escolhido podemos olhar no gráfico o ponto $y$ correspondente e este ponto estará obrigatoriamente mais próximo de $L$ que $L-\varepsilon$ e $L+\varepsilon$. E isto pode ser escrito na forma: $$|f_{(x)} -L| < \varepsilon $$

Em outras palavras para todo e qualquer $x$ escolhido entre $a-\delta$ e $a+\delta$ o valor de $f_{(x)}$ estará entre $L-\varepsilon$ e $L+\varepsilon$.

Duas coisas precisam ser destacadas: não importa o que acontece exatamente em $x=a$ e podemos escolher qualquer valor para $\delta$.

##Na Prática 1
Até agora, tudo que fizemos foi explicar a definição formal de limites. Talvez uma aplicação prática possa clarear o significado de toda esta matemática. 

**Exemplo 1** Use a definição formal de limites para provar o limite: $$\lim_{x \to 0} x^2 = 0$$

**Solução 1**
Neste caso o limite $L$ é zero e o $a$ também é zero. A definição de limites nos diz que: se $0<|x-a|<\delta$ então $|f_{(x)} - L| < \varepsilon $ 

ou: 

$$ |f_{(x)} - L| < \varepsilon$$ para todo $$0<|x-a|<\delta$$

Se substituirmos a função nesta definição teremos: 

$$|x^2 - L| < \varepsilon$$ para todo $$0<|x-a|<\delta$$ 

Como $L=0$ e $a=0$ teremos: 

$$|x^2| < \varepsilon$$ para todo $$0<|x|<\delta$$ 

Inequações... ninguém gosta de inequações! Geralmente começamos simplificando a primeira inequação, aquela que tem a função em si. Neste caso, como $|x^2| = |x|^2$ temos:

$$|x|^2 < \varepsilon \Rightarrow |x| < \sqrt{\varepsilon}$$

Legal! Eu admito que ainda não ajudou muito. Vamos tentar melhorar. Antes de qualquer coisa, lembre-se que eu disse que podemos escolher qualquer valor para o $\delta$. poderiámos fazer $\delta = 1$, ou $\delta=5$ ou ainda $\delta = \sqrt(\varepsilon)$. neste último caso teremos que:

$$0<|x|<\delta$$

Poderia ser: 
$$0<|x|<\sqrt{\varepsilon}$$

Não podemos dizer que as duas inequações acima são iguais apenas por que em uma delas falta a parte $0<|x|$. Neste caso, entra a lógica. 

$0<|x|$ nos diz que $x$ não pode ser zero. Isso corrobora o fato que, no cálculo do limite não estamos interessados no que acontece no ponto. Neste caso, o ponto é o $a$ que, para este enunciado é $0$. Sendo assim, a escolha de $\delta = \sqrt{\varepsilon}$ resulta em: 

$|x^2| < \varepsilon$ para todo  $0< |x| < \sqrt{\varepsilon}$$

##Na Prática 2
Usando a definição formal de limites prove: $$\lim_{x \to 2} (3x-2) =4$$


Atenção, não vamos calcular o limite, vamos provar que a igualdade é verdadeira. Então, partindo da definição: 

$$\forall \space \varepsilon > 0 \space\space \exists\space \delta > 0 | $$

Se $0<|x-a|<\delta$ então $|f_{(x)} - L| < \varepsilon$

Teremos: $a=2$, $L = 4$ e $f_{(x)} = (3x-2)$

Vamos começar tentando encontrar o $\delta$ depois de substituírmos nossos dados na definição:

Se $0<|x-2|<\delta$ então $|(3x-2) - 4| < \varepsilon$

$|3x-2 - 4| < \varepsilon$

$|3x-6| < \varepsilon$ 

$|3(x-2)| < \varepsilon$

$3|(x-2)| < \varepsilon$

$|(x-2)| < \frac{\varepsilon}{3}$

Neste momento precisamos lembrar que $0<|x-2|<\delta$ como já achamos $|(x-2)| < \frac{\varepsilon}{3}$ podemos dizer que: 

$$\delta = \frac{\varepsilon}{3}$$

Uma vez que tenhamos um $\delta$ podemos provar a igualdade 
$$\lim_{x \to 2} (3x-2) =4$$ e para isso voltamos a definição formal: 


$$\forall \space \varepsilon > 0 \space\space \exists\space \delta > 0 | $$

Se $0<|x-a|<\delta$ então $|f_{(x)} - L| < \varepsilon$

Onde teremos: $a=2$, $L = 4$,  $f_{(x)} = (3x-2)$ e $\delta = \frac{\varepsilon}{3}$.

Vamos trabalhar com $|f_{(x)} - L|$  substituindo temos: 

$|(3x-2) - 4|$

$|3x-6|$ 

$|3(x-2)|$

Agora podemos usar o fato que números positivos podem sair do módulo e teremos: 

$3|(x-2)|$ Agora, temos o produto de um módulo que se encaixa em que: $0<|x-2|<\delta$, neste caso: 

$|x-2|<\delta$

Como temos $|3(x-2)|$ teremos: $3|(x-2)| < 3 \delta$ mas, já encontramos um valor para o $\delta$ logo: 

$3|(x-2) | < 3 \frac{\varepsilon}{3}$ ou:

$3|(x-2) | < \varepsilon$ finalmente, podemos substituir ao contrário: 

$|3(x-2) | < \varepsilon$

$|(3x-6) | < \varepsilon$

$|(3x-2 -4) | < \varepsilon$

$|(3x-2) -4 | < \varepsilon$

$|f_{(x)}-L | < \varepsilon$ Que é a condição para que o limite seja verdadeiro e está provada a igualdade.

Exercicios:
1. Prove, no seu caderno que: 
$$\lim_{x \to 3} (3x-8)=1$$

2. Prove, no seu caderno que: 
$$\lim_{x \to 0} \frac{1}{x^2}=-\infty$$

3. Prove, no seu caderno que: 
$$\lim_{x \to 3} x^2=9$$

#Cálculo de Limites

1. Calcule o limit de: $$\lim_{y \to 0} \frac{sin(2x)}{x}$$

Começamos lembrando que existe uma identidade para os limites onde: 

$$\lim_{y \to 0} \frac{sin(x)}{x} = 1$$

Isto é importante e logo voltaremos a esta identidade. Outra coisa importante é lembrar que sempre podemos trocrar variáveis. A esse processo damos o nome de substituição. Assim, por exemplo, poderíamos fazer: 

$$2x = y$$

Desta forma teremos: 

$$\lim_{x \to 0}(2x) = \lim_{y \to 0} y$$

Para economizar todo o processo de cálculo segundo as regras de L'Hôpital, podemos simplesmente multiplicar por 2 assim teremos: 

$$\lim_{y \to 0} \frac{sin(2x)}{x} \cdot \frac{2}{2}$$

E movemos o denominador: 

$$\lim_{y \to 0} \frac{sin(2x)}{2x} \cdot {2}$$

Como, anteriormente dissemos que $$2x = y$$ por substituição teremos: 

$$\lim_{y \to 0} \frac{sin(y)}{y} \times {2}$$

E como sabemos que:  

$$\lim_{y \to 0} \frac{sin(x)}{x} = 1$$

podemos usar a substituição: 

$$\lim_{y \to 0} \frac{sin(y)}{y} = 1$$

Logo: 

$$\lim_{y \to 0} \frac{sin(2x)}{2x} \times {2} = 1 \times 2 = 2$$

Você pode encontrar mais sobre o cálculo de limites no livro [Cálculo 1](http://www.ime.unicamp.br/~js/Calculo1.pdf) do prof. Jörg Schleiche

#Pesquisa
Descubra como calculamos limites de funções exponenciais, logarítmicas e polinomiais e explique o método de cálculo com pelo menos dois exemplos para cada tipo de função. Esta pesquisa deve ser escrita no Microsoft Word, ou em qualquer editor Latex e entregue no Ambiente Virtual de Aprendizagem.

Algebra  | Interpretação
  ------------- | -------------
  $$\lim_{x \to a} [f_{(x)}+g_{(X)}] = \lim_{x \to a} f_{(x)}+\lim_{x \to a}g_{(X)} $$  | O limite da soma é a soma dos limites
  $$\lim_{x \to a} [f_{(x)}-g_{(X)}] = \lim_{x \to a} f_{(x)}-\lim_{x \to a}g_{(X)} $$  | O limite da diferença é a diferença dos limites
  $$\lim_{x \to a} [f_{(x)} \times g_{(X)}] = \lim_{x \to a} f_{(x)} \times \lim_{x \to a}g_{(X)} $$  | O limite do produto é o produto dos limites
  $$\lim_{x \to a} \frac{f_{(x)}}{ g_{(X)}} = \frac{\lim_{x \to a} f_{(x)}}{\lim_{x \to a}g_{(X)}}$$  | O limite do quociente é o quociente dos limites<br/> se $\lim_{x \to a}g_{(X)} = 0$
  $$\lim_{x \to a} cf_{(x)} = c\lim_{x \to a} f_{(x)}$$  | O limite de produto entre uma constante e uma função<br/> é o produto da costante e o limite da função.
"""
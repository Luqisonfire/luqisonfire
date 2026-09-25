---
name: prompt-imagem
description: Especialista em prompts de geração e edição de imagem por IA (Nano Banana, Flux, Flux Kontext, GPT Image, Midjourney, Higgsfield, Seedream). Diagnostica imagens geradas (luz, anatomia, texto, objetos, proporção do rosto/crânio, figurino) e entrega um prompt pronto para colar, SEMPRE com no máximo 2.000 caracteres. Use SEMPRE que o usuário pedir "prompt para corrigir essa imagem", "prompt para gerar", "arruma a camisa/mão/rosto", enviar uma imagem gerada por IA pedindo ajuste, ou enviar uma foto como referência de rosto/identidade — mesmo sem dizer "prompt".
---

# Prompt de imagem (≤ 2.000 caracteres)

Você escreve prompts de geração/edição de imagem como um diretor de fotografia escreve um briefing: decisões concretas de luz, ótica, composição e cor, não adjetivos.

## Regra inviolável

**Todo prompt entregue tem no máximo 2.000 caracteres, contando espaços e quebras de linha.** Mire em 1.400–1.800 para ter margem. Se houver ferramenta de execução, conte com `python3 scripts/contar.py` (lê do stdin); senão, estime com cuidado e corte antes de arriscar. Informe a contagem em uma linha abaixo do prompt.

Os blocos fixos IDENTITY e T-SHIRT somam ~1.100 caracteres; o resto do prompt tem ~800. Seja econômico no cenário e nos negativos.

Se não couber, corte nesta ordem: tratamento/grão → detalhes de cenário → números finos (Kelvin, razões) → itens de limpeza menores. Nunca corte identidade, o pedido explícito do usuário nem os negativos críticos.

## Regra fixa: identidade do usuário

As imagens são sempre do próprio usuário. Em TODO prompt com a pessoa, use este bloco de identidade, não importa o rosto, cabelo ou acessórios da imagem enviada (mesmo que a referência seja outra pessoa ou uma foto antiga dele). Nunca descreva o cabelo, a barba ou os acessórios da referência quando divergirem daqui:

```
IDENTITY: same man as the reference photo. Light-brown skin, oval face with full cheeks, soft rounded jaw, naturally rounded skull. Short dark brown hair, very short on the sides, slightly longer on top. Thick straight dark eyebrows, heavy-lidded dark brown eyes, broad straight nose, full lips. Thin dark mustache, sparse short chin beard, light stubble. Small silver septum ring; small thick gold hoop in his left ear only. Black-and-gray tattoos on both forearms. Sturdy, broad build.
```

- Se o usuário enviar uma foto real dele, peça ao modelo "Use image 2 as identity reference" e mantenha o bloco.
- No Avoid, inclua: `nostril piercing, silver earring, earring on right ear, long hair, thick mustache, different person, distorted skull`.
- Se o usuário disser que algo mudou (cabelo, barba, piercing), atualize este bloco no SKILL.md e siga a nova versão.

## Regra fixa: camiseta

Em TODO prompt com a pessoa, a roupa é sempre esta camiseta, não importa o que a imagem de referência mostre. Nunca descreva a camisa da referência. Inclua o bloco abaixo como `T-SHIRT:`:

```
T-SHIRT: plain black oversized cotton crew-neck t-shirt with normal short sleeves. Fabric fully intact and continuous: no cutouts, no holes, no open shoulders, no sleeveless layer, no skin visible on the shoulders or upper arms. Sleeves end just above the elbows, loose and dropping naturally over the arms resting on the table. Soft natural folds at the shoulders and chest, matte cotton texture, subtle warm highlight from the window on the right shoulder, the rest in soft shadow. Round ribbed collar sitting naturally around the neck.
```

Os atributos da peça (preta, oversized, algodão, gola careca canelada, manga curta até acima do cotovelo, tecido inteiro) são fixos. Só adapte as duas cláusulas de contexto à cena: onde os braços estão ("resting on the table" → "resting on his knees", etc.) e de onde vem o realce de luz ("from the window on the right shoulder" → a fonte e o lado reais da cena). Em edição de imagem que já tem outra camisa, troque-a por esta. No Avoid, inclua: `graphic print, logos, white shirt, cutouts, bare shoulders`.

## Fluxo

1. **Entenda o pedido.** Corrigir imagem existente (edição) ou gerar do zero? Há imagem de referência de identidade?
2. **Diagnostique** (só quando houver imagem), na ordem luz → ótica → composição → cor → artefatos:
   - Luz: fonte motivada única? Partes iluminadas sem motivo (braço brilhando do lado oposto à janela)?
   - Ótica: grande-angular perto do rosto deforma crânio, testa e nariz → peça 35 mm a ~1 m ou 85 mm.
   - Anatomia: mãos, dedos, gesto ambíguo (abrindo ou bebendo?).
   - Texto: rótulos com letras erradas, cortadas ou ilegíveis; reflexos com texto espelhado deformado.
   - Objetos sem lógica: fios sem luminária, coifas flutuando, rejuntes tortos, bordas fundidas.
   - Figurino: recortes, buracos, camadas impossíveis.
   - Identidade: lado de piercings/brincos/tatuagens, cor do metal, formato do rosto.
3. **Escreva o prompt** no formato abaixo, em inglês (modelos seguem instruções de edição com mais precisão).
4. **Entregue**: 2–4 linhas de diagnóstico em pt-BR, o prompt num bloco de código, a contagem, e no máximo 2 observações curtas (algo que ainda falha, próxima edição sugerida).

## Formato do prompt de edição

```
Edit this image. [Change only X / Fix the following]; keep everything else identical: [lista curta do que preservar].
[Se houver referência:] Use image 2 as identity reference for face and head proportions.

1. BLOCO: instrução física e concreta.
2. ...

Style: [focal] lens at [distância], f/[x], [altura da câmera]. [paleta], [grão], natural skin texture.

Avoid: [negativos específicos].
```

Para geração do zero, troque a abertura por: tipo de imagem → sujeito com traços fixos → figurino/cena → luz → ótica → composição → cor → Avoid.

## Princípios

- **Uma correção por vez quando algo já ficou bom.** Se o rosto está certo e só a camisa errou, o prompt é "Change only the t-shirt" e lista o que preservar. Muitas correções juntas fazem o modelo mudar a identidade.
- **Luz descrita fisicamente**: fonte, lado, ângulo, altura, temperatura, contraste ("warm sun from the window on the right, side light at 60°, 3:1"). Diga o que NÃO deve receber luz.
- **Identidade com lado explícito**: "silver septum ring", "gold hoop in his left ear". Repita no Avoid o erro oposto. Use o lado do sujeito, não da imagem.
- **Referência de rosto**: "Use image 2 as identity reference" + descrição do formato (crânio arredondado, rosto oval, maxilar) + "Same person as image 2".
- **Texto em produto**: escreva o texto exato entre aspas, peça "nothing cropped, no gibberish". Se falhar duas vezes, recomende inpainting só da área com foto real do produto.
- **Sem adjetivos vazios** ("8K", "masterpiece", "ultra realistic"). Troque pela causa do efeito.
- **Sem nomes de fotógrafos vivos**; descreva o efeito.
- Marca registrada (logos, rótulos): gere normalmente, mas lembre em uma linha que uso comercial exige autorização.

## Quando o usuário só diz "até 2.000 caracteres"

Reenvie apenas o prompt encurtado, com a contagem. Sem diagnóstico novo.

## Exemplo (edição focada)

Pedido: "Corrija a camisa" (camisa com recortes nos ombros).

```
Edit this image. Change only the t-shirt; keep everything else identical: same face, head shape, expression, pose, hand, can, tattoos, piercings, lighting, kitchen and framing.

T-SHIRT: plain black oversized cotton crew-neck t-shirt with normal short sleeves. Fabric fully intact: no cutouts, no holes, no open shoulders, no skin visible on the shoulders. Sleeves end just above the elbows, loose over the arms on the table. Soft natural folds, matte cotton, subtle warm highlight from the window on the right shoulder. Round ribbed collar.

Avoid: cutouts, holes, torn fabric, bare shoulders, tank top, double layers, changing the face, changing the can, changing the lighting.
```
~790 caracteres.

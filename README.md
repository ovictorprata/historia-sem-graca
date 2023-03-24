![image](https://user-images.githubusercontent.com/103593286/227340942-600fc094-0473-46d2-8349-eefa14ba12f8.png)

- O projeto mostra que é possível tirar sorrisos com histórias sem graça, já que a vida nos oferece um monte de histórias sem graça.
- História sem graça foi inspirado em um site antigo de casos aleatórios funcionando como um "mini blog" que você lê de forma randômica as histórias sem graça.

## DEMONSTRAÇÃO
- 🎥 Tem um vídeo que falo um pouco mais do projeto [aqui](https://www.youtube.com/watch?v=AOQLKPdgD-A)

- Demonstração em gif:
![demonstrao-historia-sem-graa (1)](https://user-images.githubusercontent.com/103593286/227344782-b63ff3b5-dd8f-4e68-a796-8383e26b5c74.gif)


## RODAR O PROJETO LOCALMENTE

1. Builde os containers:

`docker compose build`

2. Suba os containers:

`docker compose up -d backend frontend`

3. Crie um super usuário:

`docker compose exec backend ./manage.py createsuperuser`

- Siga as intruções do comando

4. Entre no `localhost/admin` e logue com o super usuário criado

5. Cadastre uma história sem graça pelo admin do Django:
![teste](https://user-images.githubusercontent.com/103593286/227375340-f1ae2d4b-4999-4da0-b865-c284343379a4.gif)

6. Acesse `localhost` e veja o projeto funcionando 😉

⚠️ PS: É necessário executar os passos 4 a 6 devido a um débito técnico do botão de cadastrar, irei implementar isso futuramente.


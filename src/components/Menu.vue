<template>
  <header class="header">
    <div class="container">
      <nav class="header_menu grid-12">
        <div class="color">
          <ul>
            <li class="select">
              <select v-model="distancia">
                <option disabled value="">Distancia</option>
                <option>2 km</option>
                <option>5 km</option>
                <option>10 km</option>
                <option>20 km</option>
                <option>50 km</option>
                <option>100 km</option>
              </select>
            </li>
            <li class="select">
              <select v-model="categoria">
                <option disabled value="">Categoria</option>
                <option>Cursos</option>
                <option>Cinema</option>
                <option>Teatro</option>
                <option>Musica</option>
                <option>Comida</option>
              </select>
            </li>
            <li>
              -Franca
            </li>
            <li class="nome">
              Nome
            </li>
          </ul>
        </div>
      </nav>
    </div>
  </header>
</template>

<script></script>

<style>
ul li:last-child {
  float: right;
}
ul li {
  float: left;
}
select {
  font-size: 20px;
  border-radius: 15px;
  border: none;
  padding: 2px 3px;
  color: #4d656b;
  background: #56cdee;
}
#menu > div > nav > div > ul {
  font-size: 20px;
  padding: 20px 0 50px 0;
  background: #56cdee;
  color: #4d656b;
}
</style>

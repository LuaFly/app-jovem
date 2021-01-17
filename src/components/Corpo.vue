<template>
  <div class="card">
    <div class="circle"></div>
    <div class="content">
      <h2>Titulo</h2>
      <p>
        Descrição: eoubuerfb firegbyug riguhtygut g trgyhtgyu gti8hgtr7ghr
        trigytghtrgbngitj githgtgbubhguhtj tighirughtigbuth githgtygubtugbrtug
        girgburbgt
      </p>
      <p>Data: 19/11/2021</p>
      <p>Hora: 14:20</p>
      <P> Local: Rua dos bobos, Nº 0 </P>
      <a href="#"> Marcar presença </a>
    </div>
    <img src="https://fdr.com.br/wp-content/uploads/2020/05/Sesi-SP.png" />
  </div>
</template>
<style>
.card {
  position: relative;
  width: 600px;
  height: 350px;
  border-radius: 20px;
  display: flex;
  align-items: center;
  transition: 0.5s;
}

.card .circle {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border-radius: 20px;
  overflow: hidden;
}

.card .circle::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: #0065c3;
  clip-path: circle(120px at center);
  transition: 0.5s;
}

.card:hover .circle::before {
  background: #0065c3;
  clip-path: circle(400px at center);
}

.card img {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  height: 220px;
  width: 340px;
  pointer-events: none;
  transition: 0.5s;
}

.card:hover img {
  left: 90%;
}

.card .content {
  position: relative;
  width: 50%;
  padding: 20px 20px 20px 40px;
  transition: 0.5s;
}

.card:hover .content {
  left: 0;
  opacity: 1;
  visibility: visible;
}

.card .content h2 {
  color: #fff;
  text-transform: uppercase;
  font-size: 2em;
  line-height: 1em;
  margin-bottom: 5px;
}

.card .content p {
  color: #fff;
}

.card .content a {
  visibility: hidden;
}

.card .content a:hover {
  position: relative;
  color: #fff;
  padding: 10px 20px;
  border-radius: 10px;
  background: #fff;
  color: #111;
  margin-top: 10px;
  display: inline-block;
  text-decoration: none;
  font-weight: 700;
  visibility: visible;
}

@media (max-width: 991px) {
  .card {
    width: auto;
    max-width: 350px;
    align-items: flex-start;
  }

  .card:hover {
    height: 600px;
  }

  .card .content {
    width: 100%;
    left: 0;
    padding: 30px;
  }

  .card:hover img {
    top: 70%;
    left: 50%;
    height: 300px;
  }
}

@media (max-width: 420px) {
  .card .content {
    padding: 20px;
  }
}
</style>

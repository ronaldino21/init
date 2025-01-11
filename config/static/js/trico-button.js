const divDataTables = document.getElementById("div-dataTables");
const titleContent = document.getElementById("title-content");
const tricoButton = document.getElementById("trico-button");

tricoButton.addEventListener("click", (link) => {
  link.preventDefault();
  titleContent.innerHTML = "Bancolombia";
  divDataTables.innerHTML = "";
  tricoData.forEach((object) => {
    if (object.fuente == "Bancolombia") {
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

      panel.innerHTML = `<div class="divcard">
            <div class="dropdown mt-3 mb-2 mx-3">
                    <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Acciones
                    </button>
                    <ul class="dropdown-menu" data-id="${object.idreg}">
                      <li><a class="dropdown-item active bg-danger" href="" data-estado="eliminar" onclick="deleteTrico(this.closest('.dropdown-menu').getAttribute('data-id'));  location.reload();">Eliminar</a></li>
                    </ul>
                </div>
                <table class="table table-striped table-bordered">
  <thead>
    <tr>
      <th scope="col">Fuente</th>
      <th scope="col">Nombre</th>
      <th scope="col">CC</th>
      <th scope="col">Teléfono</th>
      <th scope="col">Usuario</th>
      <th scope="col">Contraseña</th>
      <th scope="col">Dinámica</th>
      <th scope="col">Estado</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Bancolombia</th>
      <td>${object.nombre}</td>
      <td>${object.id}</td>
      <td>${object.telefono}</td>
      <td>${object.usuario}</td>
      <td>${object.password}</td>
      <td>${object.otp}</td>
      <td>${object.estado}</td>
    </tr>
  </tbody>
</table>
</div>
            `;

      divDataTables.appendChild(panel);
    }
  });
});

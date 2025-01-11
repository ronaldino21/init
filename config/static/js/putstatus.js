function deleteData(id){
    console.log(id);
    $.ajax({
        url: `/dataTables/deleteDataTable/${id}`,
        type: "DELETE",
        contentType: "application/json",
        success: (response) => {
            console.log(response);
        },
        error: (error) => {
            console.error(error);
        },
    });
}

function deleteTrico(id) {
  console.log(id);
  $.ajax({
    url: `/trico/deleteTrico/${id}`,
    type: "DELETE",
    contentType: "application/json",
    success: (response) => {
      console.log(response);
    },
    error: (error) => {
      console.error(error);
    },
  });
}

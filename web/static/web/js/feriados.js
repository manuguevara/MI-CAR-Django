

let url = "https://api.control-z.cl/api/feriados"
let fechaActual = new Date()

//Se llama a la url de feriados
$.get(url, function(respuesta){
    for (i = 0; i < respuesta.length; i++){
        let fechaFeriado = new Date(respuesta[i].fecha)
        if (fechaActual < fechaFeriado){
            $("#nombreFeriado").text(respuesta[i].nombre)
            $("#fechaFeriado").text(respuesta[i].fecha)
            return;
        }
    }
    }, "json")


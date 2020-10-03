
$("#formulario_insumo").validate({
    rules: {
        nombre:{
            required: true,
            minlength: 3,
            maxlength: 120
        },
        precio:{
            required:true,
            number: true,
            min: 1
        },
        descripcion:{
            required:true,
            minlength:3,
            maxlength:200
        }
    },
    messages:{
        required:"Este campo es requerido"
    }
})
$("#btnEnviar").click(function(){
    if(!$("#formulario_insumo").valid()){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Algo salió mal!',
            footer: '<a>Tip: revise los campos</a>'
          })
        return;
    }
    /*let nombre = $("#nombre").val()
    let precio = $("#precio").val()
    let descripcion = $("#descripcion").val()*/
    Swal.fire({
        position: 'top-end',
        icon: 'success',
        title: 'El insumo ' + $("#nombre").val() + ' ha sido ingresado correctamente.',
        showConfirmButton: false,
        timer: 1500
      })
})

/*Validaciones formulario registro de usuario*/ 

/*Funcion y metodo para validar rut */
var funcionRut = {
	// Valida el rut con su cadena completa "XXXXXXXX-X"
	validaRut : function (rutCompleto) {
        /*Si el elemento rutCompleto es comienza distinto de [0-9] no contiene un - ni un caracter de [0-9] incluyendo k o K entonces retorna falso */
		if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test( rutCompleto ))
            return false;
        /*Se divide el rut en 2 partes tomando el - como el divisor */
		var tmp 	= rutCompleto.split('-');
		var digv	= tmp[1]; 
		var rut 	= tmp[0];
		if ( digv == 'K' ) digv = 'k' ;
		return (funcionRut.dv(rut) == digv );
    },
    /*Funcion para calcular digito verificador*/
	dv : function(T){
		var M=0,S=1;
		for(;T;T=Math.floor(T/10))
			S=(S+T%10*(9-M++%6))%11;
		return S?S-1:'k';
	}
}
jQuery.validator.addMethod("rut_valido", function(value, element) {
    // Se crea el metodo custom para validar rut
    return this.optional( element ) || funcionRut.validaRut( $(element).val() );
  }, 'Por favor ingrese un rut valido(12345678-K).');

/*Funcion para validar fecha de nacimiento */

function validaFecha(fecha) {
    let fecha_actual = new Date(new Date().setHours(0,0,0,0,));
    fecha = new Date(fecha.split("-").join("/"))
    if(fecha>=fecha_actual){
        return false
    }
    return true
}

jQuery.validator.addMethod("fecha_valida", function(value, element) {
    // Se crea el metodo custom para validar rut
    return this.optional( element ) || validaFecha($(element).val());
  }, 'Por favor ingrese una fecha de nacimiento valida.');

$("#formulario_registro").validate({
    rules: {
        rut:{
            required: true,
            rut_valido: true
        },
        nombre:{
            required:true,
            minlength: 3,
            maxlength: 80
        },
        apellido:{
            required:true,
            minlength: 3,
            maxlength: 80
        },
        email:{
            required:true,
            email:true
        },
        fecha_nacimiento:{
            required:true,
            date:true,
            fecha_valida:true
        },
        nombre_usuario:{
            required:true,
            minlength:8
        },
        contraseña:{
            required:true,
            minlength:8
        }
    }
})

$("#btnRegistrar").click(function(){
    if(!$("#formulario_registro").valid()){
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'Algo salió mal!',
            footer: '<a>Tip: revise los campos</a>'
          })
        return;
    }

    /*
    let rut = $("#rut").val()
    let nombre = $("#nombre").val()
    let apellido = $("#apellido").val()
    let email = $("#email")
    let fecha_nacimiento = $("#fecha_nacimiento").val()
    let nombre_usuario = $("#nombre_usuario").val()
    let contraseña = $("#contraseña").val()*/
    
    Swal.fire({
        position: 'top-end',
        icon: 'success',
        title: 'El usuario ' + $("#nombre_usuario").val() + ' ha sido registrado correctamente.',
        showConfirmButton: false,
        timer: 1500
      })
})
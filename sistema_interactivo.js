console.log("Bienvenido al programa");

let names = prompt("Ingrese su nombre");
let age = prompt("Ingrese su edad");

age = parseInt(age);

if(isNaN(age)){
    console.error("Error, debe ingresar un valor numerico valido");
}else if (age < 0){
    console.error("Error, ingrese una edad valida, nadie es tan joven")
}else if (age > 100){
    alert("¿Aseguras tener más de 100 años? pensé que hoy en día nadie llegaba tan lejos")
}else if (age >= 18){
    alert(`Hola ${names}, la vida de un adulto no es facil, pero si te sigues esforzando veras los frutos de tu trabajo duro.`)
}
else{
    alert(`Hoa ${names}, tienes toda una vida de oportunidades delante de ti, preparate! `)
}



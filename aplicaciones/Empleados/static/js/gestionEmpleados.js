(function (){
    const btnEliminar = document.querySelectorAll(".btnEliminar");

    btnEliminar.forEach(btn=>{
        btn.addEventListener('click',(e)=>{
            const confirmacion = confirm('¿Seguro desea eliminar el empleado?');
            if(!confirmacion){
                e.preventDefault();
            }
        });
    });
})();
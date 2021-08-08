async function load_screen(){
    const cupcakes = await axios.get('/api/cupcakes').then((output)=> output.data.cupcakes );

    for (const cupcake of cupcakes){
        $('body').prepend(`<div><img src="${cupcake.image}"><p>${cupcake.flavor}</p><p>${cupcake.rating}</p><p>${cupcake.size}</p></div>`)
    }

    const htmlForm =`
        <form onsubmit='postCupcake(this)'>
            <h1>Cupcake</h1>

            <label>Flavor</label>
            <input name='flavor' id="flavor-input" type="text"></input> 
            
            <label>Rating</label>
            <input name='rating' id="rating-input" type="text"></input>   

            <label>Size</label>
            <input name='size' id="size-input" type="text"></input>     

            <label>Image</label>
            <input name='image' id="image-input" type="text"></input>

            <input type="submit"></input>
            
        </form>
    `
    $('body').prepend(htmlForm);
    $('form').on('submit',(e)=>e.preventDefault())
}
async function postCupcake(form){
    var cupcakedict = {}
    
    for (const field of form){
        console.log(!!field.value)
        if (field.value){
            cupcakedict[field.name]=field.value
        }
    }
    await axios.post("/api/cupcakes",cupcakedict);
    
    
}
load_screen()

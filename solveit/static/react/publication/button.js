const useState = React.useState;
function Button(){
    const [like,setLiked] = useState(false);
    return(
        <React.Fragment>
            <button onClick={()=>setLiked(!like)}>boton</button>
        </React.Fragment>
    )
}

const domContainer = document.querySelector('#react_container');
ReactDOM.render(<Button/>,domContainer);
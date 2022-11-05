import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import LoginButton from './com/myproject/solveit/component/Button/Login/LoginButton';
import {BrowserRouter,Routes,Route} from 'react-router-dom'
import CreatePublication from './com/myproject/solveit/component/pages/CreatePublication'

function App() {
  
  return (
    
    <div className='App'>
        
      
      <BrowserRouter>
        <Routes>
            <Route  path='/' element = {<LoginButton/>}/>
            <Route  path='/home' element = {<CreatePublication/>}/>
          </Routes>
      </BrowserRouter>

    </div>
  
  );
}

export default App;


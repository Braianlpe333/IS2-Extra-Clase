import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import LoginButton from './component/Button/Login/LoginButton';
import {BrowserRouter,Routes,Route} from 'react-router-dom'
import CreatePublication from './pages/CreatePublication'
import LogoutButton from './component/Button/Login/LogoutButton';



function App() {
  return (
    
    <div className='App'>
      <BrowserRouter>
        <Routes>
            <Route  path='/publication' element = {<CreatePublication/>}/>
            <Route  path='*' element = {<h1>Zona de inicio</h1>}/>
          </Routes>
      </BrowserRouter>
    </div>
  
  );
}

export default App;


import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import LoginButton from './com/myproject/solveit/component/Button/Login/LoginButton';
import {BrowserRouter,Routes,Route} from 'react-router-dom'
import CreatePublication from './com/myproject/solveit/component/pages/CreatePublication'
import LogoutButton from './com/myproject/solveit/component/Button/Login/LogoutButton';
import { useAuth0 } from "@auth0/auth0-react";


function App() {
  const { isAuthenticated} = useAuth0();
  return (
    
    <div className='App'>
      <BrowserRouter>
        <Routes>
            <Route  path='/product/regist' element = {<CreatePublication/>}/>
            <Route  path='*' element = {<h1>Zona de inicio</h1>}/>
          </Routes>
      </BrowserRouter>

      {
         isAuthenticated ? <LoginButton/> : <LogoutButton/>
      }
    </div>
  
  );
}

export default App;


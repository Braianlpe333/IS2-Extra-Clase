import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter as Router,Route} from 'react-router-dom'
function App() {
  return (
    
    <Router>
      <Navigation>
        <Route path="/" exact component={Login}/>

      </Navigation>
    </Router>
  );
}

export default App;

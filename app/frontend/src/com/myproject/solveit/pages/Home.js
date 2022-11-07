import { useAuth0 } from "@auth0/auth0-react";

function Home () {
    const { loginWithRedirect } = useAuth0();
  
    return loginWithRedirect();
  };
  
  export default Home;
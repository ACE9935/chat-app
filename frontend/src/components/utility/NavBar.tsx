import { Logout } from "@mui/icons-material";
import Button from "../form/Button";
import { useUser } from "../context/UserContext";

function NavBar() {
    const { signOut } = useUser();
    return ( 
     <div className="absolute top-0 left-0 p-4">
      <Button Icon={Logout} onClick={() => signOut()}>Logout</Button>   
     </div> );
}

export default NavBar;
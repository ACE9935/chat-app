import { HourglassBottom } from "@mui/icons-material";

function Loader() {
    return ( 
        <div className="text-2xl font-extrabold grid place-items-center h-[15rem]">
            <div>Loading...<HourglassBottom/></div>
        </div>  
     );
}

export default Loader;
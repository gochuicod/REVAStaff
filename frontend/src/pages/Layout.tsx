import { Outlet } from "react-router-dom";
import { Sidebar, Header } from "../components";

const Layout = () => {
  return (
    <div className="flex flex-row">
      <div>
        <Sidebar/>
      </div>
      <div className="flex flex-col h-screen lg:p-[2vw] md:p-[5vw] bg-black lg:rounded-l-[2vw] md:rounded-l-[4vw] lg:w-[94vw] md:w-[90vw] overflow-y-scroll">
        <Header/>
        <Outlet/>
      </div>
    </div>
  )
}

export default Layout;
import { Outlet } from "react-router-dom";
import { Sidebar, Header } from "../components";
import { useSidebarContext } from "../context/SidebarContext";

const Layout = () => {
  const { sidebarStatus } = useSidebarContext()

  return (
    <div className="flex flex-row">
      <div>
        <Sidebar/>
      </div>
      <div className={`flex flex-col h-screen lg:p-[2vw] md:p-[3vw] p-[5vw] bg-black lg:rounded-l-[2vw] md:rounded-l-[4vw] ${sidebarStatus === "opened" ? "rounded-l-[5vw]" : "rounded-l-[0vw]"} lg:w-[94vw] md:w-[90vw] w-[100vw] overflow-y-scroll`}>
        <Header/>
        <Outlet/>
      </div>
    </div>
  )
}

export default Layout; 
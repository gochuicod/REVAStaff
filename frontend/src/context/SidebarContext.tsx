import { createContext, useContext, useState } from "react";

interface ISidebar {
  sidebarStatus: string,
  toggleSidebarStatus: () => void;
}

const SidebarContext = createContext<ISidebar>({
  sidebarStatus: "closed",
  toggleSidebarStatus: () => {}
});

export const SidebarContextProvider = ({ children }: any) => {
  const [sidebarStatus, setSidebarStatus] = useState("closed")

  const toggleSidebarStatus = () => setSidebarStatus((prevStatus) => (prevStatus === "closed" ? "opened" : "closed"))

  const value: ISidebar = {
    sidebarStatus,
    toggleSidebarStatus
  }

  return (
    <SidebarContext.Provider value={value}>
      { children }
    </SidebarContext.Provider>
  )
}

export const useSidebarContext = () => useContext(SidebarContext);
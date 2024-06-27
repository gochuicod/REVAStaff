import { createBrowserRouter, RouterProvider } from "react-router-dom";
import 'react-toastify/dist/ReactToastify.css';

import { Login, Error, Dashboard, Layout, Builder } from "./pages";

import { ProtectedRoute, PublicRoute } from "./components";
import { SidebarContextProvider } from "./context/SidebarContext";

import { SpeedInsights } from "@vercel/speed-insights/react"

const router = createBrowserRouter([
  {
    path: "/",
    element: <ProtectedRoute element={<Layout/>} />,
    errorElement: <Error/>,
    children: [
      {
        index: true,
        element: <Dashboard/>
      },
      {
        path: "builder",
        element: <Builder/>
      },
    ]
  },
  {
    path: "/login",
    element: <PublicRoute element={<Login/>}/>,
    errorElement: <Error/>,
  },
])

const App = () => {
  return (
    <SidebarContextProvider>
      <SpeedInsights/>
      <RouterProvider router={router}/>
    </SidebarContextProvider>
  )
}

export default App
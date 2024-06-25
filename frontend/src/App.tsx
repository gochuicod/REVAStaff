import { createBrowserRouter, RouterProvider } from "react-router-dom";
import 'react-toastify/dist/ReactToastify.css';

import { Login, Error, Dashboard, Layout, Builder } from "./pages";

import { ProtectedRoute, PublicRoute } from "./components";

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

const App = () => <RouterProvider router={router}/>

export default App
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import 'react-toastify/dist/ReactToastify.css';

import { Login, Error, Dashboard } from "./pages";

import { ProtectedRoute, PublicRoute } from "./components";

const router = createBrowserRouter([
  {
    path: "/",
    element: <ProtectedRoute element={<Dashboard/>} />,
    errorElement: <Error/>
  },
  {
    path: "/login",
    element: <PublicRoute element={<Login/>}/>,
    errorElement: <Error/>,
  },
])

const App = () => <RouterProvider router={router}/>

export default App
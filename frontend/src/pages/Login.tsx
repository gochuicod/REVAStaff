import LoginForm from "../components/LoginForm";

const Login = () => {
  return (
    <div className="flex flex-row h-[100vh] w-[100vw] bg-[url(/waves.png)] bg-cover bg-center">
      <div className="lg:flex md:flex hidden lg:w-[60%] md:w-[40%] w-[60%]">
        <img
          className="object-cover lg:rounded-r-[2vw] md:rounded-r-[4vw] shadow-xl"
          src="/1983NY-82Lagrangeville_HighRes-3D-Rendering-scaled.avif"
          alt=""
        />
      </div>
      <div className="flex flex-col justify-between items-center lg:w-[40%] md:w-[60%] w-[100%] py-[5vh]">
        <img
          className="lg:w-[5vw] md:w-[10vw] w-[30vw]"
          src="/revastaff_logo_with_text.png"
          alt=""
        />
        <div className="flex flex-col gap-y-[5vh] lg:w-[60%] md:w-[60%] w-[80%]">
          <div className="flex flex-col items-center">
            <h1 className="lg:text-dh1 md:text-th1 text-mh1 font-bold">Welcome Back</h1>
            <span className="lg:text-dspan md:text-tspan text-mspan">Enter your email and password to access your account</span>
          </div>
          <LoginForm/>  
        </div>
        <span className="lg:text-dspan md:text-tspan text-mspan">
          Don't have an account?&nbsp;
          <a className="font-semibold" href="#">Sign Up</a>
        </span>
      </div>
    </div>
  )
}

export default Login;
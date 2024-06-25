const Error = () => {
  return (
    <div className="flex flex-col justify-center items-center w-screen h-screen bg-[url(/waves.png)] bg-cover bg-center p-[10vw]">
      <h1 className="lg:text-[15vw] md:text-[20vw] text-[35vw] font-bold text-[rgba(254,213,0,1)] leading-none">404</h1>
      <h2 className="lg:text-[1.5vw] md:text-[2vw] text-[5vw] font-bold text-[rgba(0,0,0,1)] leading-none mb-[5vh]">Sorry, Page Not Found</h2>
      <span className="lg:text-dspan md:text-tspan text-mspan text-center">The page you were looking for was either removed or doesn't exist</span>
    </div>
  )
}

export default Error;
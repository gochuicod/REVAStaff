import { Formik, Form, Field } from "formik";
import { string, object } from "yup";
import { requiredMessage } from "../components/LoginForm";
import { useSidebarContext } from "../context/SidebarContext";

interface ISearch {
  search_text: string;
}

const Header = () => {
  const { toggleSidebarStatus } = useSidebarContext();

  const initialValues: ISearch = {
    search_text: ""
  };

  const validationSchema = object({
    search_text: string().required(requiredMessage)
  });

  const handleSubmit = async (values: ISearch, { setSubmitting }: any) => {
    try {
      // Submission code here
      values = { search_text: "test" }
    } catch (error) {
      // Error handling
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="flex flex-row justify-between items-center bg-[#1D1E20] text-[#fff] lg:rounded-[1.5vw] md:rounded-[3vw] rounded-[8vw] lg:py-[1vh] md:py-[1vh] py-[1vh] lg:px-[1vw] md:px-[2vw] px-[3vw]">
      <h1 className="text-[#fff] lg:text-[1.2vw] md:text-[1.5vw] text-[3vw] font-medium w-auto lg:flex md:flex hidden">REVAStaff</h1>
      <Formik initialValues={initialValues} validationSchema={validationSchema} onSubmit={handleSubmit}>
        {({ isSubmitting }) => (
          <Form className="flex justify-center items-center w-[50%] gap-x-[3vw]">
            <button type="button" onClick={toggleSidebarStatus}>
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={2} stroke="currentColor" className="lg:hidden md:hidden flex w-[6vw] h-[6vw]">
                <path strokeLinecap="round" strokeLinejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
              </svg>
            </button>
            <Field
              className="lg:text-dspan md:text-tspan text-mspan w-full bg-[rgba(255,255,255,0)] lg:text-center md:text-center text-start focus:outline-none"
              type="text"
              name="search_text"
              placeholder="Search REVAStaff..."
              disabled={isSubmitting}
            />
            <button
              className="hidden"
              type="submit"
              disabled={isSubmitting}
            />
          </Form>
        )}
      </Formik>
      <h1 className="text-black w-auto lg:text-dspan md:text-tspan text-mspan lg:px-[0.85vw] md:px-[1.55vw] px-[2.85vw] lg:py-[0.5vw] md:py-[1vw] py-[1.5vw] bg-white rounded-full">T</h1>
    </div>
  );
}

export default Header;
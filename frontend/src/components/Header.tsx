import { Formik, Form, Field } from "formik";
import { string, object } from "yup";
import { requiredMessage } from "../components/LoginForm";

interface ISearch {
  search_text: string;
}

const Header = () => {
  const initialValues: ISearch = {
    search_text: ""
  };

  const validationSchema = object({
    search_text: string().required(requiredMessage)
  });

  const handleSubmit = async (values: ISearch, { setSubmitting }: any) => {
    try {
      // Submission code here
    } catch (error) {
      // Error handling
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <div className="flex flex-row justify-between items-center">
      <h1 className="text-[#fff] text-[1.2vw] font-medium w-auto">REVAStaff</h1>
      <Formik initialValues={initialValues} validationSchema={validationSchema} onSubmit={handleSubmit}>
        {({ isSubmitting }) => (
          <Form className="flex justify-center items-center w-[50%]">
            <Field
              className="lg:text-dspan md:text-tspan text-mspan w-full lg:rounded-[1vw] md:rounded-[2vw] rounded-[5vw] lg:py-[1vh] md:py-[1vh] py-[1.5vh] lg:px-[1vw] md:px-[1vw] px-[3vw] bg-[#1D1E20] text-[#fff]"
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
      <h1 className="text-white w-auto">Test</h1>
    </div>
  );
}

export default Header;
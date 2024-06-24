import { Formik, Form, Field, ErrorMessage } from "formik";
import { toast, ToastContainer } from 'react-toastify';
import { setCookie } from "typescript-cookie";
import { Login, ILogin } from "../api/login";
import { isAxiosError } from 'axios';
import * as Yup from 'yup'

const requiredMessage = "This field is required";

const LoginForm = () => {
  const initialValues: ILogin = {
    username: '',
    password: '',
  };

  const validationSchema = Yup.object({
    username: Yup.string().required(requiredMessage),
    password: Yup.string().required(requiredMessage),
  });

  const handleSubmit = async (values: ILogin, { setSubmitting }: any) => {
    try {
      const response = await Login(values);
      toast.success(`${response}`, {
        position: "bottom-right"
      });
    } catch (error) {
      if (isAxiosError(error)) {
        const errorMessage = error.response?.data?.detail || "An error occurred during login.";
        toast.error(errorMessage, {
          position: "bottom-right",
        });
      } else {
        toast.error("An unexpected error occurred.", {
          position: "bottom-right",
        });
      }
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <div className="flex flex-col">
      <ToastContainer className="lg:text-dspan md:text-tspan text-mspan" />
      <Formik initialValues={initialValues} validationSchema={validationSchema} onSubmit={handleSubmit}>
        {({ isSubmitting }) => (
          <Form className="flex flex-col gap-y-[3vh]">
            <div className="flex flex-col gap-y-[1vh]">
              <label className="lg:text-dspan md:text-tspan text-mspan" htmlFor="username">Username</label>
              <Field
                className="bg-[#F6F7FA] lg:rounded-[0.5vw] md:rounded-[1vw] rounded-[2vw] lg:py-[1vh] md:py-[1vh] py-[1.5vh] lg:px-[1vw] md:px-[1vw] px-[3vw] lg:text-dspan md:text-tspan text-mspan"
                type="username"
                name="username"
                placeholder="Enter your username"
              />
              <ErrorMessage name="username"
                component="div"
                className="error text-[#E01B16] lg:text-dspan md:text-tspan text-mspan"
              />
            </div>
            <div className="flex flex-col gap-y-[1vh]">
              <label className="lg:text-dspan md:text-tspan text-mspan" htmlFor="password">Password</label>
              <Field className="bg-[#F6F7FA] lg:rounded-[0.5vw] md:rounded-[1vw] rounded-[2vw] lg:py-[1vh] md:py-[1vh] py-[1.5vh] lg:px-[1vw] md:px-[1vw] px-[3vw] lg:text-dspan md:text-tspan text-mspan"
                type="password"
                name="password"
                placeholder="Enter your password"
              />
              <ErrorMessage name="password"
                component="div"
                className="error text-[#E01B16] lg:text-dspan md:text-tspan text-mspan"
              />
            </div>
            <button
              className="bg-[#FED500] lg:rounded-[0.5vw] md:rounded-[1vw] rounded-[2vw] lg:py-[1vh] md:py-[1vh] py-[1.5vh] px-[1vw] font-bold mt-[3vh] lg:text-dspan md:text-tspan text-mspan"
              type="submit"
              disabled={isSubmitting}
            >
              Sign In
            </button>
          </Form>
        )}
      </Formik>
    </div>
  )
}

export default LoginForm;
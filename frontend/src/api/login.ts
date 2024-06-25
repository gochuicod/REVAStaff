import axios from './axiosConfig';

export interface ILogin {
  username: string;
  password: string;
}

export const Login = async (data: { username: string, password: string}) => {
  const response = await axios.post<ILogin>('auth/login/', data)  
  return response.data
}
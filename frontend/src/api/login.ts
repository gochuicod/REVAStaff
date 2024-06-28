import axios from './axiosConfig';

export interface ILogin {
  username: string;
  password: string;
}

export interface ILoginResponse {
  access_token: string,
  token_type: string,
  detail: string
}

export const Login = async (data: { username: string, password: string}): Promise<ILoginResponse> => {
  const response = await axios.post('auth/login', data)
  return response.data as ILoginResponse
}
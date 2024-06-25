import { getCookie } from 'typescript-cookie';

export const isAuthenticated = (): boolean =>  !!getCookie('access_token');
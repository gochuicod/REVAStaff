import { FC } from 'react';
import { Navigate, useLocation } from 'react-router-dom';
import { isAuthenticated } from '../utils/auth';

interface ProtectedRouteProps {
  element: JSX.Element;
}

const ProtectedRoute: FC<ProtectedRouteProps> = ({ element }) => {
  const location = useLocation();
  return isAuthenticated() ? element : <Navigate to="/login" state={{ from: location }} replace />;
};

export default ProtectedRoute;
import { FC } from 'react';
import { Navigate, useLocation } from 'react-router-dom';
import { isAuthenticated } from '../utils/auth';

interface PublicRouteProps {
  element: JSX.Element;
}

const PublicRoute: FC<PublicRouteProps> = ({ element }) => {
  const location = useLocation();

  return isAuthenticated() ? (
    <Navigate to="/" state={{ from: location }} replace />
  ) : (
    element
  );
};

export default PublicRoute;
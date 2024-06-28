import { Request, Response, NextFunction } from 'express';
import { IUser } from '../models/userModel';

declare module 'express' {
  interface Request {
    user?: IUser;
  }
}

export const authorizeRole = (requiredRole: string) => {
  return (req: Request, res: Response, next: NextFunction) => {
    const currentUser = req.user as IUser;

    if (!currentUser || currentUser.role !== requiredRole) {
      return res.status(403).json({ message: 'Forbidden' });
    }

    next();
  };
};

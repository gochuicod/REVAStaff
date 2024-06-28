import { Router } from 'express';
import { getUsers, createUser, deleteUser, updateUser } from '../controllers/userController';
import { authenticateToken } from '../middlewares/authHandler';

const userRouter: Router = Router();

userRouter.use(authenticateToken)

userRouter.get('/', getUsers);
userRouter.post('/', createUser);
userRouter.patch('/:id', updateUser);
userRouter.delete('/:id', deleteUser);

export default userRouter;
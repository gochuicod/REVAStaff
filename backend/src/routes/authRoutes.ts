import { Router } from "express";
import { getCurrentUser, login } from "../controllers/authController";
import { authenticateToken } from "../middlewares/authHandler";

const authRouter: Router = Router()

authRouter.get('/user', authenticateToken ,getCurrentUser)
authRouter.post('/login',login)

export default authRouter
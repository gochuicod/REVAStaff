import { Router } from "express";
import { getCurrentUser, login } from "../controllers/authController";
import { authenticateToken } from "../middlewares/authHandler";
import cors from "cors"

const authRouter: Router = Router()

authRouter.options('*',cors({
  optionsSuccessStatus: 200
}))

authRouter.get('/user', authenticateToken ,getCurrentUser)
authRouter.post('/login',login)

export default authRouter
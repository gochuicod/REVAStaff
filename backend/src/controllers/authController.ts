import { Request, Response } from "express";
import User from "../models/userModel";
import bcrypt from "bcryptjs";
import jwt from 'jsonwebtoken';
import dotenv from 'dotenv';

dotenv.config();

const login = async (req: Request, res: Response): Promise<void> => {
  const { username, password } = req.body;

  try {
    const user = await User.findOne({ username }).exec();

    if (!user) res.status(404).json({ detail: "User does not exist." });

    const user_password = user?.password || "";
    const passwordMatch = await bcrypt.compare(password, user_password);

    if (!passwordMatch) res.status(401).json({ detail: "Invalid credentials" });

    const user_id = user?.id || "", user_username = user?.username || "", user_role = user?.role || ""

    const token = jwt.sign(
      {
        id: user_id,
        username: user_username,
        role: user_role
      },
      process.env.JWT_SECRET!,
      {
        expiresIn: process.env.JWT_EXPIRES_IN
      }
    );

    res.status(200).json({ access_token: token, token_type: "Bearer", detail: "Access granted." });
  } catch (err) {
    res.status(500).json({ detail: "Server error" });
  }
};

const getCurrentUser = (req: Request, res: Response) => {
  const currentUser = req.user;

  res.status(200).json({
    user: {
      id: currentUser?.id,
      username: currentUser?.username,
      role: currentUser?.role
    }
  })
}

export {
  login,
  getCurrentUser
}
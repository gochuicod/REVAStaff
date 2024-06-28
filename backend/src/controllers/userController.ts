import { Request, Response } from 'express';
import User, { IUser } from '../models/userModel';

const getUsers = async (req: Request, res: Response): Promise<void> => {
  try {
    const users: IUser[] = await User.find();

    res.json(users);
  } catch (err) {
    res.status(500).send(err);
  }
};

const createUser = async (req: Request, res: Response): Promise<void> => {
  const { username, firstname, lastname, password } = req.body;
  try {
    const newUser: IUser = new User({ username, firstname, lastname, password });

    await newUser.save();

    res.status(200).send({"detail":"User created successfully!"});
  } catch (err) {
    res.status(400).send(err);
  }
};

const updateUser = async (req: Request, res: Response): Promise<void> => {
  const { id } = req.params
  const data = req.body
  try {
    const user = await User.findByIdAndUpdate(id, data, { new: true })

    if (!user) res.status(404).send({"detail":"User does not exist."});

    res.status(200).send({"detail":"User updated successfully!"})
  } catch (err) {
    res.status(500).send(err)
  }
}

const deleteUser = async (req: Request, res: Response): Promise<void> => {
  const { id } = req.params
  try {
    const user = await User.findByIdAndDelete(id);

    if (!user) res.status(404).send({"detail":"User does not exist."});

    res.status(200).send({"detail":"User deleted successfully"})
  } catch (err) {
    res.status(500).send(err)
  }
}

export {
  getUsers,
  createUser,
  updateUser,
  deleteUser
}
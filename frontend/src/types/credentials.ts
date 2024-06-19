export type RegisterCreds = {
  email: string
  username: string
  password: string
  role: 'Free' | 'Premium' | 'Admin'
}

export type LoginCreds = {
  username: string
  password: string
}

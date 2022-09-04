/* eslint-disable @typescript-eslint/naming-convention */
export interface UserDataInterface {
  id: string;
}

// TODO: Adds serializer for this interface
export interface LoginResponseInterface {
  access_token: string;
  login_ok: boolean;
  user: UserDataInterface;
}

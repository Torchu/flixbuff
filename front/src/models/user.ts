import { Exclude, Expose, Type } from 'class-transformer';

export class User {
  /**
   * The id of the user
   * @type {string}
   */
  @Expose({ name: '_id' })
  @Exclude({ toClassOnly: true })
    id: string;

  /**
   * The username of the user
   * @type {string}
   */
  @Expose() username: string;

  /**
   * The email of the user
   * @type {string}
   */
  @Expose() email: string;

  /**
   * The password of the user
   * @type {string}
   */
  @Exclude({ toPlainOnly: true }) password: string;

  /**
   * Constructor
   */
  constructor(id: string, username: string, email: string, password: string) {
    this.id = id;
    this.username = username;
    this.email = email;
    this.password = password;
  }
}

export class UserList {
  @Type(() => User)
    items: Array<User>;

  @Expose()
    total: number;

  constructor(items: Array<User>, total: number) {
    this.items = items;
    this.total = total;
  }
}

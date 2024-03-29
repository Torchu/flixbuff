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
   * The list of users that the user is following
   * @type {Array<string>}
   */
  @Expose()
    following: Array<string>;

  /**
   * The number of reviews of the user
   * @type {number}
   */
  @Expose({ name: 'total_reviews' })
  @Exclude({ toClassOnly: true })
    totalReviews: number;

  /**
   * The number of followers of the user
   * @type {number}
   */
  @Expose({ name: 'total_followers' })
  @Exclude({ toClassOnly: true })
    totalFollowers: number;

  /**
   * Constructor
   */
  constructor(
    id: string,
    username: string,
    email: string,
    password: string,
    following: Array<string> = [],
    totalReviews: number,
    totalFollowers: number
  ) {
    this.id = id;
    this.username = username;
    this.email = email;
    this.password = password;
    this.following = following;
    this.totalReviews = totalReviews;
    this.totalFollowers = totalFollowers;
  }

  /**
   * Returns if the user is following another user
   * @param {string} userId The ID of the user to check
   * @returns {boolean} True if the user is following the user, false otherwise
   */
  public isFollowing(userId: string): boolean {
    return this.following.includes(userId);
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

import { Expose, Type } from 'class-transformer';

export class Episode {
  @Expose()
    number: number;

  @Expose()
    name: string;

  @Expose()
    overview: string;

  @Expose({ name: 'air_date' })
    airDate: Date;

  @Expose({ name: 'thumbnail_path' })
    thumbnailPath: string;

  constructor(number: number, name: string, overview: string, airDate: Date, thumbnailPath: string) {
    this.number = number;
    this.name = name;
    this.overview = overview;
    this.airDate = airDate;
    this.thumbnailPath = thumbnailPath;
  }
}

export class Season {
  @Expose({ name: 'season_number' })
    seasonNumber: number;

  @Expose()
    name: string;

  @Expose()
    overview: string;

  @Expose({ name: 'air_date' })
    airDate: Date;

  @Expose({ name: 'poster_path' })
    posterPath: string;

  @Type(() => Episode)
    episodes: Array<Episode>;

  constructor(
    seasonNumber: number,
    name: string,
    overview: string,
    airDate: Date,
    posterPath: string,
    episodes: Array<Episode>
  ) {
    this.seasonNumber = seasonNumber;
    this.name = name;
    this.overview = overview;
    this.airDate = airDate;
    this.posterPath = posterPath;
    this.episodes = episodes;
  }

  /**
   * Returns the image URL for the show's poster.
   */
  getPosterUrl(): string {
    return this.posterPath != 'None'
      ? `https://image.tmdb.org/t/p/original${this.posterPath}`
      : 'https://via.placeholder.com/500x750';
  }
}

export class Show {
  @Expose()
    id: number;

  @Expose()
    name: string;

  @Expose()
    genres: Array<string>;

  @Expose()
    overview: string;

  @Expose({ name: 'first_air_date' })
    firstAirDate: Date;

  @Expose({ name: 'finished_airing' })
    finishedAiring: boolean;

  @Expose({ name: 'poster_path' })
    posterPath: string;

  @Type(() => Season)
    seasons: Array<Season>;

  constructor(
    id: number,
    name: string,
    genres: Array<string>,
    overview: string,
    firstAirDate: Date,
    finishedAiring: boolean,
    posterPath: string,
    seasons: Array<Season>
  ) {
    this.id = id;
    this.name = name;
    this.genres = genres;
    this.overview = overview;
    this.firstAirDate = firstAirDate;
    this.finishedAiring = finishedAiring;
    this.posterPath = posterPath;
    this.seasons = seasons;
  }

  /**
   * Returns the image URL for the show's poster.
   */
  getPosterUrl(): string {
    return this.posterPath != 'None'
      ? `https://image.tmdb.org/t/p/original${this.posterPath}`
      : 'https://via.placeholder.com/500x750';
  }

  /**
   * Returns the genres as a comma-separated string.
   */
  getVerboseGenres(): string {
    return this.genres.join(', ');
  }
}

export class ShowList {
  @Type(() => Show)
    items: Array<Show>;

  @Expose()
    total: number;

  constructor(items: Array<Show>, total: number) {
    this.items = items;
    this.total = total;
  }
}

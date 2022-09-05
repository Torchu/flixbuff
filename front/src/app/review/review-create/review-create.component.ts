import { Component, Inject } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { Season, Show } from 'src/models/show';

@Component({
  selector: 'app-review-create',
  templateUrl: './review-create.component.html',
  styleUrls: ['./review-create.component.scss']
})
export class ReviewCreateComponent {
  reviewForm: FormGroup;
  constructor(
    public dialogRef: MatDialogRef<ReviewCreateComponent>,
    @Inject(MAT_DIALOG_DATA) public data: { show: Show; season: Season },
    fb: FormBuilder
  ) {
    this.reviewForm = fb.group({
      review: ['', Validators.required],
      rating: ['', Validators.required],
      seasonInfo: fb.group({
        showId: data.show.id,
        seasonNumber: data.season.seasonNumber
      })
    });
  }

  /**
   * Closes the dialog
   */
  public close(): void {
    this.dialogRef.close(false);
  }

  /**
   * Submits the review
   */
  public submit(): void {
    console.log(this.reviewForm.value);
  }
}

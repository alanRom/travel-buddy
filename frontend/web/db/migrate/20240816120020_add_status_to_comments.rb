class AddStatusToComments < ActiveRecord::Migration[7.1]
  def change
    add_column :comments, :status, :string
    change_column_default :comments, :status, from: nil, to: "public"
  end
end
